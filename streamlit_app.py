import streamlit as st
tab1,tab2 = st.tabs(['Current values', 'History'])
with tab1:
  st.markdown(f''' <html>
<head>
<title>Data Collection Dashboard</title>
<style>
    button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
body
    {
        width:70%;
        margin-left:auto;
        margin-right:auto;
    }
</style>
</head>
<body>
    <a href="value.html">
        <button>Current Values</button>
      </a>
      
<table border=2 bordercolor="#0000FF">
<tr><td colspan="2">
<h1 align="center" color="#00FFFF">Data Collection Dashboard</h1>
</td></tr>
<tr><td>
    <iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1843031/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Methane+%28MQ4%29&type=line&xaxis=Time&yaxis=PPM"></iframe>
</td>
<td><iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1843031/charts/2?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Carbon+Monoxide+%28MQ7%29&type=line&xaxis=Time&yaxis=PPM"></iframe>
</td></tr>
<tr><td>
    <iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1843031/charts/3?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Sulphur+%28MQ135%29&type=line&xaxis=Time&yaxis=PPM"></iframe></td></tr>

</html>
''',unsafe_allow_html=True)
