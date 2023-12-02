`timescale 1ns/1ps

module final_msd;

 logic dimm_clk=1,cpu_clk=1;
 
 initial
  begin 
         forever #1.03125 cpu_clk = ~cpu_clk; // CPU_CLOCK
         //forever #2.0625 dimm_clk = ~dimm_clk; // DIMM_CLOCKr
  end
 initial  forever #2.0625 dimm_clk = ~dimm_clk; // DIMM_CLOCKr

 int counter_c,counter_d;
 logic [75:0] y,w;
 logic flag;
 logic [75:44] time_temp;
 
 logic [75:0]queue[$:15];
 
 logic [35:0]temp;
 logic [35:0]temp_t,abc;
 logic [3:0] operation_t;
 logic [3:0] op,op_t;
 logic [31:0]time_t,time_o;
 logic [31:0]time_t_p=0;
 logic [3:0] core_t,core_o;
 logic [31:0]time_t1,time_o1;
 logic [3:0] core_t1,core_o1;

int Trcd=39,Tcl=40,Trp=39,Tburst=8;
int timing_t;
int count=0;
int dimm_count=0;


int Trp_delay,Trcd_delay,Tcl_delay,Tburst_delay;
int rd2data,wr2data;
 
    logic [1:0] byte_sel,byte_sel_t;
	logic [5:2] column_l,column_l_t;
	logic channel,channel_t;
	logic [9:7] bank_g,bank_gt;
	logic [11:10] bank,bank_t;
	logic [17:12] column_h,column_h_t;
	logic [33:18] row,row_t;
	
	logic [9:7] bank_temp_p,bank_g_temp_p,bank_temp,bank_g_temp;
	

typedef struct {
    logic [31:0] cpu_time;
    logic [31:0] core;
    logic [1:0] operation;
    logic [33:0] address;
  } record;
  
record var1;


logic [9:7] bank_group_v;
logic [11:10] bank_v;

  
function void push(input [35:0]x, input [3:0]y, input [31:0]z,input [3:0] a);
  w = {z,a,y,x};   //z=time,  a=core  y=operation  x = address
  queue.push_back(w);
  //$fwrite(trace_out,"\n ______________________\npushed queue value is %h ->  at cpu_clk = %d\n dimm_clk= %d\n*********************\n The Time: %d\n core  %d\n operation  %d\n address  %h\n ______________________ ",w,counter_c,counter_d,w[75:44],w[43:40],w[39:36],w[35:0]);
  $fwrite(trace_out,"pushed queue value is %h --- at cpu_clk = %d --- dimm_clk= %d \n",w,counter_c,counter_d);
  $display("*********************");
  $fwrite(trace_out,"\n pushed value Bank_group = %d -- bank = %d\n",w[9:7],w[11:10]);
  if(queue.size()==16) 
   $fwrite(trace_out,"**********************************************************************queue is full\n");
   
endfunction
  
     integer trace_in,trace_out;
	 string inp_filename,out_filename; 
  
 initial 
 begin
 
	if($value$plusargs("inp_filename=%s",inp_filename))
	 $display("new_file_name_by_user = %s",inp_filename);
	else
	 begin
	   inp_filename="trace.txt";
	 end
	 
	 if($value$plusargs("out_filename=%s",out_filename))
	 $display("new_output_file_name_by_user = %s",out_filename);
	else
	 begin
	   out_filename="my_output_final.txt";
	 end
	 
	trace_in = $fopen(inp_filename,"r");
	trace_out= $fopen(out_filename,"w");
	
	 if(!trace_in)
	  $display("File_cannot_open");
	  
	 while(!$feof(trace_in))
	  begin
	 // @(posedge cpu_clk)
	   //begin
	     if(queue.size()<16)
   		  begin
           $fscanf(trace_in,"%d %d %d %h",var1.cpu_time,var1.core,var1.operation,var1.address);
		 
		 `ifdef DEBUG_PARSE
		   $fwrite(trace_out,"*****************************************\nCPU_TIME:--> %0d || CORE:--> %0d || OPERATION:--> %0d || ADDRESS:--> %0h\n*********************************************",var1.cpu_time,var1.core,var1.operation,var1.address);
		  //$display("cpu_time : %d \t core : %d  \t operation : %d  \t address: %h",var1.cpu_time,var1.core,var1.operation,var1.address);
		 `endif
 

		op = var1.operation;	 //operation	
	    temp = var1.address;     // address
		core_t = var1.core;      // core
		time_t = var1.cpu_time;  // time
        
		
		
        bank_t = temp[11:10];
        bank_gt= temp[9:7];
        row_t = temp[35:18];
        column_h_t= temp[17:12];
        column_l_t= temp[5:2];
		channel_t = temp[6];
		byte_sel_t = temp[1:0];
		
		bank_temp = bank_t;
		bank_g_temp = bank_gt;
		
		if({bank_g_temp,bank_temp} == {bank_g_temp_p,bank_temp_p})
   		 begin
		  flag = 1;
		 end
		 
		if(flag)
		   begin
		   // timing_t = counter_d;
			//Trp_delay = timing_t+Trp;
			repeat(Trp)
			 begin
			    @(posedge dimm_clk);
			 end
			 flag=0;
		  end
		 // repeat(time_t)
		  //  @(posedge cpu_clk);
	      // push({row_t,column_h_t,bank_t,bank_gt,channel_t,column_l_t,byte_sel_t},op,time_t,core_t);
		
		if(op == 0)
   		 begin   
		    $fwrite(trace_out,"************************************************\n");
		    $fwrite(trace_out,"*****************READ_OPERATION******************\n");
		    $fwrite(trace_out," %d  %d  ACT0  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,row_t);
		    $fwrite(trace_out," %d  %d  ACT1  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,row_t);

           // Trcd_delay = counter_d+Trcd;
		    repeat(Trcd)
			 begin
			    @(posedge dimm_clk);
			 end
			
		    $fwrite(trace_out," %d  %d  RD0  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,column_h_t);
		    $fwrite(trace_out," %d  %d  RD1  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,column_h_t);
		   
		    rd2data=Tcl+Tburst; 
		    repeat(rd2data)
			  begin
			    @(posedge dimm_clk);
			  end
            $fwrite(trace_out," %d  %d  PRE  %d  %d \n",counter_c,channel_t, bank_gt,bank_t);	
            //@(posedge dimm_clk)   
		      // y=queue.pop_front();
			  
		       /* y=queue.pop_front();
                bank_g_temp_p=y[9:7];
		        bank_temp_p=y[11:10]; 
                $fwrite(trace_out,"The poped output is %h at cpu_clk=%d dimm_clk=%d\n",y,counter_c,counter_d);
			    $fwrite(trace_out,"The poped  bank group = %d  and bank = %d \n",bank_g_temp_p,bank_temp_p);
		       
			   */
		    //bank_g_temp_p=y[9:7];
		    //bank_temp_p=y[11:10];
		 end 
		 
		else if(op == 1)
   		 begin   
		    $fwrite(trace_out,"************************************************\n");
		    $fwrite(trace_out,"*****************write_OPERATION******************\n");
		    $fwrite(trace_out," %d  %d  ACT0  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,row_t);
		    $fwrite(trace_out," %d  %d  ACT1  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,row_t);

           // Trcd_delay = counter_d+Trcd;
		    repeat(Trcd)
			 begin
			    @(posedge dimm_clk);
			 end
			
			
		    $fwrite(trace_out," %d  %d  WR0  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,column_h_t);
		    $fwrite(trace_out," %d  %d  WR1  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,column_h_t);
		    
		    rd2data=Tcl+Tburst; 
		    repeat(rd2data)
			  begin
			    @(posedge dimm_clk);
			  end
            $fwrite(trace_out," %d  %d  PRE  %d  %d \n",counter_c,channel_t, bank_gt,bank_t);	
            //@(posedge dimm_clk)   
		      // y=queue.pop_front();
			  /*
		        y=queue.pop_front();
                bank_g_temp_p=y[9:7];
		        bank_temp_p=y[11:10]; 
                $fwrite(trace_out,"The poped output is %h\n",y,counter_c,counter_d);
			    $fwrite(trace_out,"The poped  bank group = %d  and bank = %d \n",bank_g_temp_p,bank_temp_p);
		      */
			   
		    //bank_g_temp_p=y[9:7];
		    //bank_temp_p=y[11:10];
		 end

        else if(op == 2)
   		  begin   
		    $fwrite(trace_out,"************************************************\n");
		    $fwrite(trace_out,"*****************Fetch_OPERATION******************\n");
		    $fwrite(trace_out," %d  %d  ACT0  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,row_t);
		    $fwrite(trace_out," %d  %d  ACT1  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,row_t);

            //Trcd_delay = counter_d+Trcd;
		    repeat(Trcd)
			 begin
			    @(posedge dimm_clk);
			 end
			
		    $fwrite(trace_out," %d  %d  RD0  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,column_h_t);
		    $fwrite(trace_out," %d  %d  RD1  %d  %d  %h\n",counter_c,channel_t, bank_gt,bank_t,column_h_t);
		    
		    rd2data=Tcl+Tburst; 
		    repeat(rd2data)
			  begin
			    @(posedge dimm_clk);
			  end
            $fwrite(trace_out," %d  %d  PRE  %d  %d \n",counter_c,channel_t, bank_gt,bank_t);	
            //@(posedge dimm_clk) 
             //begin
               //if(queue.size()!=0) begin
			   /*
		        y=queue.pop_front();
                bank_g_temp_p=y[9:7];
		        bank_temp_p=y[11:10]; 
                $fwrite(trace_out,"The poped output is %h\n",y,,counter_c,counter_d);
                $fwrite(trace_out,"The poped  bank group = %d  and bank = %d \n",bank_g_temp_p,bank_temp_p);   
		      */
		  end 
		   
		        @(posedge dimm_clk)
 				 begin
		           y=queue.pop_front();
                   bank_g_temp_p=y[9:7];
		           bank_temp_p=y[11:10]; 
                   $fwrite(trace_out,"The poped output is %h\n",y,,counter_c,counter_d);
                   $fwrite(trace_out,"The poped  bank group = %d  and bank = %d \n",bank_g_temp_p,bank_temp_p);   
        		 end
	    end
		
	// end
	  end
	  $fclose(trace_in);
 
 end
 
 
 
 always@(posedge cpu_clk) 
  begin
  
  if($value$plusargs("inp_filename=%s",inp_filename))
	 $display("new_file_name_by_user = %s",inp_filename);
	else
	 begin
	   inp_filename="trace.txt";
	 end
	 
	 if($value$plusargs("out_filename=%s",out_filename))
	 $display("new_output_file_name_by_user = %s",out_filename);
	else
	 begin
	   out_filename="my_output_final.txt";
	 end
  
  	trace_in = $fopen(inp_filename,"r");
	trace_out= $fopen(out_filename,"w");
	
	if(!trace_in)
	  $display("File_cannot_open");
     
	while(!$feof(trace_in))
	 begin
	    	     if(queue.size()<16)
   		            begin
                      $fscanf(trace_in,"%d %d %d %h",var1.cpu_time,var1.core,var1.operation,var1.address);
					  
					  op = var1.operation;	 //operation	
	                  temp = var1.address;     // address
		              core_t = var1.core;      // core
		              time_t = var1.cpu_time;  // time
        
		
		
                      bank_t = temp[11:10];
                      bank_gt= temp[9:7];
                      row_t = temp[35:18];
                      column_h_t= temp[17:12];
                      column_l_t= temp[5:2];
		              channel_t = temp[6];
		              byte_sel_t = temp[1:0];
		
		              bank_temp = bank_t;
		              bank_g_temp = bank_gt;
					  
					   repeat((time_t)-(time_t_p))
					    begin
						 @(posedge cpu_clk);
						end
						push({row_t,column_h_t,bank_t,bank_gt,channel_t,column_l_t,byte_sel_t},op,time_t,core_t);
						time_t_p = var1.cpu_time;
	                end
					
			     else
				   begin
				    
					@(posedge dimm_clk);
				   
				   end
	 end
	 	  //$fclose(trace_in);

  end
 
 
 
 always@(posedge cpu_clk)
  begin
     counter_c = counter_c+1;
  end
 always@(posedge dimm_clk)
  begin
     counter_d = counter_d+1;
  end
  

endmodule