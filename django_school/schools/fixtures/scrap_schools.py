from pyquery import PyQuery as pq

urls = [
	'http://103.251.43.156/schoolfixation/index.php/Publicview/index/schoolsdetails/',
	'https://oruschool.in/india/pkhs-manjapra-school-kannambra',	
	'http://www.schoolsworld.in/schools/showschool.php?school_id=32060200110',
	]

my_html= '''
&#13;
&#13;
<table width="500" align="center" class="table-condensed table-striped" border="1">&#13;
  &#13;
  <tr style="font-weight:bold" bgcolor="#CC99FF" align="center"><td>School Code</td><td>District</td><td>Educational District</td><td>Sub District</td></tr>&#13;
       <!--  <tr><th>Name of School</th><td><b>47445 : ALPS PULLALOOR NORTH</b></td></tr>-->&#13;
  <tr align="center"><td>47445</td><td>Kozhikode</td><td>Thamarassery</td><td>Koduvally</td></tr>&#13;
    <!--    <tr><th>District</th><td>Kozhikode</td></tr>
        <tr><th>Educational District</th><td>Thamarassery</td></tr>
        <tr><th>Sub District</th><td>Koduvally</td></tr>-->&#13;
       &#13;
&#13;
</table>&#13;
 </div> 



<div class=" panel-info">&#13;
<div class="panel-heading"> <h3 class="panel-title"><b>Basic School Information</b></h3></div>&#13;
</div>&#13;
&#13;
<br/>&#13;
<table align="center" width="500" class="table-condensed table-striped" border="1" style="border-collapse:inherit">&#13;
	&#13;
	<tr align="center"><td>School Establishment Date : </td><td>Not Available</td></tr>&#13;
	<tr align="center"><td>Total School Area : </td><td>0.145 hectare / acre</td></tr>&#13;
	<tr align="center"><td>Total No. of Rooms : </td><td>4</td></tr>&#13;
	<tr align="center"><td>Total Teaching Staff : </td><td>3</td></tr>&#13;
	<tr align="center"><td>Total Non-Teaching Staff : </td><td>0</td></tr>&#13;
	&#13;
	<!--<tr  align='center'><td>School Establishment Date : </td><td></td></tr>-->&#13;
	&#13;
	&#13;
	&#13;
    <!--<tr  align='center'><td>Class</td><td>Strength</td></tr>
        
             <tr align='center'><td>1</td><td>17</td></tr>
       
                <tr align='center'><td>2</td><td>17</td></tr>
       
                <tr align='center'><td>3</td><td>11</td></tr>
       
                <tr align='center'><td>4</td><td>6</td></tr>
       
            <tr bgcolor='#FFFFCC' align='center'><td>Total</td><td>51</td></tr>
    -->&#13;
     &#13;
</table>


<!--<center><h3>Class Wise Student Strength</h3></center>-->&#13;
<div class=" panel-info">&#13;
<div class="panel-heading"> <h3 class="panel-title"><b>Class Wise Student Strength 2014-15</b> </h3></div></div>&#13;
    <br/>&#13;
<table align="center" width="500" class="table-condensed table-striped" border="1" style="border-collapse:inherit">&#13;
        <tr style="font-weight:bold" align="center">&#13;
            <td>Class</td>&#13;
            <td>Strength (<span style="color:green;">2014 - 2015</span>) Based on Sixth Working day</td>&#13;
            <td>Strength (<span style="color:green;">2014 - 2015</span>) Based on Sampoorna</td>&#13;
            <td>Total available UID</td>&#13;
             <td>Valid UID</td>&#13;
             <td>Partialy Match UID</td>&#13;
               <td>Invalid UID</td>&#13;
               <td>None</td>&#13;
        </tr>&#13;
        &#13;
            <tr align="center"><td>1</td>&#13;
         <!--   <td><a href="http://103.251.43.156/schoolfixation/index.php/reportUids/index/1/1">17</a></td>-->&#13;
        &#13;
            <td>17</td>&#13;
            <td>17</td>&#13;
            <td>7</td>&#13;
 <td>4</td>&#13;
       <!--     <td>
<a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/valid/1">
4</a>
</td> -->&#13;
            &#13;
            <td>&#13;
                   -            &#13;
            </td>&#13;
            &#13;
            <td>&#13;
                   -            &#13;
            </td>&#13;
            <td>&#13;
                   <!--<a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/none/1"></a>-->&#13;
                    10            &#13;
            </td>&#13;
            &#13;
   <!--         <td><a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/invalid/1">-</a></td>
            
            <td><a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/none/1">10</a></td>
-->&#13;
        </tr>&#13;
       &#13;
                <tr align="center"><td>2</td>&#13;
         <!--   <td><a href="http://103.251.43.156/schoolfixation/index.php/reportUids/index/1/2">17</a></td>-->&#13;
        &#13;
            <td>17</td>&#13;
            <td>17</td>&#13;
            <td>17</td>&#13;
 <td>12</td>&#13;
       <!--     <td>
<a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/valid/2">
12</a>
</td> -->&#13;
            &#13;
            <td>&#13;
                   -            &#13;
            </td>&#13;
            &#13;
            <td>&#13;
                   <!--<a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/invalid/2"></a>-->&#13;
                    1            &#13;
            </td>&#13;
            <td>&#13;
                   -            &#13;
            </td>&#13;
            &#13;
   <!--         <td><a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/invalid/2">1</a></td>
            
            <td><a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/none/2">-</a></td>
-->&#13;
        </tr>&#13;
       &#13;
                <tr align="center"><td>3</td>&#13;
         <!--   <td><a href="http://103.251.43.156/schoolfixation/index.php/reportUids/index/1/3">11</a></td>-->&#13;
        &#13;
            <td>11</td>&#13;
            <td>11</td>&#13;
            <td>11</td>&#13;
 <td>11</td>&#13;
       <!--     <td>
<a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/valid/3">
11</a>
</td> -->&#13;
            &#13;
            <td>&#13;
                   -            &#13;
            </td>&#13;
            &#13;
            <td>&#13;
                   -            &#13;
            </td>&#13;
            <td>&#13;
                   -            &#13;
            </td>&#13;
            &#13;
   <!--         <td><a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/invalid/3">-</a></td>
            
            <td><a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/none/3">-</a></td>
-->&#13;
        </tr>&#13;
       &#13;
                <tr align="center"><td>4</td>&#13;
         <!--   <td><a href="http://103.251.43.156/schoolfixation/index.php/reportUids/index/1/4">6</a></td>-->&#13;
        &#13;
            <td>6</td>&#13;
            <td>6</td>&#13;
            <td>6</td>&#13;
 <td>6</td>&#13;
       <!--     <td>
<a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/valid/4">
6</a>
</td> -->&#13;
            &#13;
            <td>&#13;
                   <!--<a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/partialy/4"></a>-->&#13;
                    1            &#13;
            </td>&#13;
            &#13;
            <td>&#13;
                   -            &#13;
            </td>&#13;
            <td>&#13;
                   -            &#13;
            </td>&#13;
            &#13;
   <!--         <td><a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/invalid/4">-</a></td>
            
            <td><a href="http://103.251.43.156/schoolfixation/index.php/Publicview/index/uidDetails/1/none/4">-</a></td>
-->&#13;
        </tr>&#13;
       &#13;
                   <tr style="font-weight:bold" bgcolor="#FFFFCC" align="center"><td>Total</td><td>51</td>&#13;
           <td>51</td>&#13;
            <td>41</td>&#13;
               <td>33</td>&#13;
&#13;
                <td>1</td>&#13;
                &#13;
               <td>1</td>&#13;
                 &#13;
               <td>10</td>&#13;
&#13;
           </tr>&#13;
             &#13;
    </table>&#13;
<br/>    &#13;
    &#13;
<div class=" panel-info">&#13;
<div class="panel-heading"> <h3 class="panel-title" style="color:red;font-size:15px;"><b>Disclaimer</b> </h3></div>&#13;
    <br/> <span style="color:red; font-size:14px;margin-left:20px;">&#13;
    This UID data verified with support of IT Mission. &#13;
        Above mentined  UID is not perfectly matching with actual UID data.&#13;
       Error occur due to partial name matching, Name difference, Date of Birth difference.&#13;
</span>&#13;
<br/><br/>&#13;
&#13;
 &#13;
&#13;
    &#13;
<div class=" panel-info">&#13;
<div class="panel-heading">&#13;
    &#13;
    &#13;
    <h3 class="panel-title"><b>&#13;
	<a href="#" onclick="show('2014-15')"><b title="Click to view staff fixation strength 2014-15" id="fix2014-15" style="background-color:;">Staff Fixation Strength 2014-15</b></a> <b> | </b>&#13;
	<a href="#" onclick="show('2010-11')"><b title="Click to view staff fixation strength 2010-11" id="fix2010-11" style="background-color:;">Staff Fixation Strength 2010-11</b></a>&#13;
   </b>  </h3>&#13;
    &#13;
</div></div>&#13;
   <!-- <br>
    <table align="center" width="500" class="table-condensed table-striped" border="1" style="border-collapse:inherit">
    <tr style="font-weight:bold"  align='center'><td>Designation Name</td><td>Strength (<span style="color:green;">2010 - 2011</span>)</td></tr>
       
                  <tr>
          <td>Head Master</td>
          <td align='center'>1</td>
          </tr>
                  <tr>
          <td>Junior Language FT Arabic (LP) </td>
          <td align='center'>1</td>
          </tr>
                  <tr>
          <td>LPSA</td>
          <td align='center'>3</td>
          </tr>
            <tr style="font-weight:bold" bgcolor='#FFFFCC' ><td align='center'><b>Total</b></td><td align='center'><b>5</b></td></tr>
    </table> 
    -->&#13;
    <br/>&#13;
&#13;
<div id="2014-15">&#13;
    <table align="center" width="500" class="table-condensed table-striped" border="1" style="border-collapse:inherit">&#13;
    <tr style="font-weight:bold" align="center"><td>Designation Name</td><td>Strength (<span style="color:green;">2014 - 2015</span>)</td></tr>&#13;
       &#13;
                  <tr>&#13;
          <td>Headmaster (Primary)</td>&#13;
          <td align="center">1</td>&#13;
          </tr>&#13;
                  <tr>&#13;
          <td>Junior Language Teacher (Arabic)</td>&#13;
          <td align="center">1</td>&#13;
          </tr>&#13;
                  <tr>&#13;
          <td>L.P.S  Assistant</td>&#13;
          <td align="center">3</td>&#13;
          </tr>&#13;
            <tr style="font-weight:bold" bgcolor="#FFFFCC"><td align="center"><b>Total</b></td><td align="center"><b>5</b></td></tr>&#13;
    </table>&#13;
</div> &#13;
&#13;
<br/>&#13;
&#13;
<div id="2010-11" style="display:none;">&#13;
    <table align="center" width="500" class="table-condensed table-striped" border="1" style="border-collapse:inherit">&#13;
    <tr style="font-weight:bold" align="center"><td>Designation Name</td><td>Strength (<span style="color:green;">2010 - 2011</span>)</td></tr>&#13;
       &#13;
                  <tr>&#13;
          <td>Head Master</td>&#13;
          <td align="center">1</td>&#13;
          </tr>&#13;
                  <tr>&#13;
          <td>Junior Language FT Arabic (LP) </td>&#13;
          <td align="center">1</td>&#13;
          </tr>&#13;
                  <tr>&#13;
          <td>LPSA</td>&#13;
          <td align="center">3</td>&#13;
          </tr>&#13;
            <tr style="font-weight:bold" bgcolor="#FFFFCC"><td align="center"><b>Total</b></td><td align="center"><b>5</b></td></tr>&#13;
    </table>&#13;
</div> &#13;
<br/>&#13;
</div>&#13;
    &#13;


<!--<center><h3>Employee Details</h3></center>-->&#13;
<div class=" panel-info">&#13;
<div class="panel-heading"> <h3 class="panel-title"><b>Employee Details </b></h3></div></div>&#13;
    <br/>&#13;
<table width="100%" class="table-condensed table-striped" border="1" style="border-collapse:inherit">&#13;
   <tbody height="25%" style="">&#13;
      <tr style="background-color:#FFFFCC!important" class="table_row_first">&#13;
        <th width="29" rowspan="3" valign="top" style="font-weight:bold">Sl. No</th>&#13;
        &#13;
        <th width="30" rowspan="3" valign="top" style="font-weight:bold">Name of Employee</th>&#13;
	<th width="30" rowspan="3" valign="top" style="font-weight:bold">Designation</th>&#13;
   <!-- <th width="60" rowspan="3" valign="top"  style="font-weight:bold">Date of Birth</th>-->&#13;
     <th width="60" rowspan="3" valign="top" style="font-weight:bold">Date of Joining</th>&#13;
     <!-- <th width="60" rowspan="3" valign="top"  style="font-weight:bold">PEN</th>-->&#13;
      </tr>&#13;
      </tbody>   &#13;
           <tr> &#13;
        <td align="center">1</td>&#13;
	<td>U.K.USSAIN</td>&#13;
        <td>LPSA</td>&#13;
        &#13;
        <!--<td>08-04-1961</td>-->&#13;
        <td>11-06-1986</td>&#13;
       <!-- <td>537846</td>-->&#13;
       </tr>&#13;
           <tr> &#13;
        <td align="center">2</td>&#13;
	<td>C.MAIMOONATH</td>&#13;
        <td>LPSA</td>&#13;
        &#13;
        <!--<td>01-06-1964</td>-->&#13;
        <td>31-07-1985</td>&#13;
       <!-- <td>537842</td>-->&#13;
       </tr>&#13;
           <tr> &#13;
        <td align="center">3</td>&#13;
	<td>LEELA.B</td>&#13;
        <td>Primary HM</td>&#13;
        &#13;
        <!--<td>20-05-1960</td>-->&#13;
        <td>22-06-1981</td>&#13;
       <!-- <td>537838</td>-->&#13;
       </tr>&#13;
     &#13;
&#13;
</table>&#13;

'''
# 1 - 11000
#d = pq(url = urls[0]+'1')
#print(d)
#pq(my_html)



#scraped = pq(url = urls[0]+'1')
sample = {'district': 'Kozhikode', 
'city': 'Koduvally ', 
'name': 'School Name: ALPS PULLALOOR NORTH ', 
'code': '47445', 
'address_1': 'Thamarassery'}

class School(object):
	"""docstring for School"""
	def __init__(self):		
		self.name = ''		
		self.code = ''
		self.address_1 = ''
		self.city = ''
		self.district = ''

	def scrap_html(self,t):		
		name= t('div.panel-heading').text()
		self.name = name.lower()

		x = t('table').text().split('\n')
		self.code = x[4]
		self.address_1 = x[6].lower()
		self.city = x[7].lower()
		self.district = x[5].lower()

fp = open('datas.txt','w')
for i in range(1,5):
	s=School()
	txt = pq(url = urls[0]+str(i))
	s.scrap_html(txt)
	fp.write('{s.name}, {s.code}, {s.address_1}, {s.city}, {s.district}\n'.format(s=s))