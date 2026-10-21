<%
    // Retrieve form parameter
    String age = request.getParameter("age");
    // Check if form is submitted
    if (age == null) {
%>
<h2>Enter Voter Details</h2>
<form action="" method="post">
    Age: <input type="text" name="age"><br><br>
    <input type="submit" value="Check Eligibility">
</form>
<%
    } else {
        int voterAge = Integer.parseInt(age);
%>
<h2>Voter Eligibility Result</h2>
<%
        if (voterAge >= 18) {
%>
<p><b>Age:</b> <%= voterAge %></p>
<p><b>Status:</b> Eligible to vote</p>
<%
        } else {
%>
<p><b>Age:</b> <%= voterAge %></p>
<p><b>Status:</b> Not eligible to vote</p>
<%      }
%>
<br>
<a href="voter.jsp">Go Back</a>
<%
    }
%>