<h1>OverView</h1>
<td>
  <li>Use Scrapy Frame Work to Crawl hotel data (yilong.com only for Five Star right now).</li>
  <li>Use Selenium Webdriver to handle dynamic loaded webpage(e.g Ajax or JS).</li>
  <li>Convert Unicode to Utf-8 by Encode and Decode for the data in chinese and store in json file.</li>
</td>
<br>
<h2>Specify the Functionality of File </h2>
<td>
  <li>Path: yilong/items.py       	 # specify what kind of item you want to store (e.g link).</li>
  <li>Path: yilong/pipilines.py   	 # specify how you want to handle the data previously stored.</li>
  <li>Path: yilong/settings.py       # specify the setting you want to set.(e.g apply pipeline for spider).</li>
  <li>path: yilong/spider/spiders.py				 # specify the actual spider, this file is the major spider file.
  <li>Path: result.json  # result.json is the raw data crawled from webpage.
  <li>Path: resultFinal.json # It is raw data handled by pipelines.</li>
</td>
<h2 style="color:red;">Note</h2>

<p>Before Run the Project, Make Sure You Have Already Setup Scrapy Environment
<a href="http://doc.scrapy.org/en/latest/intro/install.html">Click to Learn How To Install Scrapy</a>
</p>

<p>Do Not Forget To Install Selenium. ($ pip install Selenium)</p>
<p>Command to Run. $ scrapy crawl spiderName -o outputFileName -t outputFileType</p>
