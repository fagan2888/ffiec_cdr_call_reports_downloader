# Real-bulk download Call Reports from FFIEC

This Python CLI program automates a Google Chrome window to access the [FFIEC's Central Data Repository public website](https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx).
I need this data for research purposes.
The FFIEC has a SOAP interface that can be used by registered users.
However, it is limited in scope because it does not allow to download **all** call reports publicly available at once.
On top of this, I am an extremely lazy researcher that totally cannot afford to manually click on all options in a HTML drop-down menu that populates a AJAX request.
Hence this program.


## Main program steps

This is a screenshot of the website that stood in my way.

![Screenshot of landing page](./img/landing.png)

It looks like a pretty easy static HTML webpage, but it is not.
As you click elements in the page, there is some Javascript code that runs in the background.
Such Javascript code silently compiles a POST request that is sent to an AJAX server.
And this is evil.
The POST request is populated with a random (to me) string that makes the returned content a puzzle (to me) to solve.

My program procedes in the following steps.

First, it opens the webpage on a new, automated Chrome window. Pretty easy. You should notice, somewhere in my code I've put the following lines:

    driverLocation = "C:/Users/apsql/.chromedriver_win32/chromedriver.exe"
    browser = webdriver.Chrome(driverLocation)

I did this because I did not want to put `chromedriver.exe` in my [PATH](https://en.wikipedia.org/wiki/PATH_(variable)).
Therefore, I specified the location of the executable on my system when calling `webdriverChrome()`.

Then, it looks for the set of options under the "_Available Products_" header.<sup>[1](#notreally)</sup> It then emulates a selection (as triggered by a human click) on the option labelled "_Call Reports -- Single Period_."

<!-- ![ListBox1](./img/select1.png) -->
<p align="center"><img src="./img/select1.png" alt="ListBox1"></p>

It ensures that the [radio button](https://en.wikipedia.org/wiki/Radio_button) related to the TSV export option is selected under "_Available File Formats_".

<!-- ![RadioButton](./img/tsvradio.png) -->
<p align="center"><img src="./img/tsvradio.png" alt="RadioButton"></p>

It retrieves _all_ available options in the drop-down menu under "_Reporting Period End Date_."

<!-- ![ListDropDown](img/select2.png) -->
<p align="center"><img src="./img/select2.png" alt="ListDropDown"></p>

Finally, one by one, it selects each of the available dates and clicks on the Download button near the top of the page.

<!-- ![DownloadButton](img/dload_button.png) -->
<p align="center"><img src="./img/dload_button.png" alt="DownloadButton"></p>


<sup><a name="#notreally">1</a>. It's not really a [header](https://www.w3schools.com/tags/tag_header.asp), it's a [`<div>`](https://www.w3schools.com/tags/tag_div.asp) with a [`<label>`](https://www.w3schools.com/tags/tag_label.asp) tag, which got the web-developer a place in hell.</sup>


## Dependencies

- [Python 3](https://www.python.org)
- [Selenium](https://www.seleniumhq.org)
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/)

My setup is on a Windows 10 machine.
I use [Anaconda](https://www.anaconda.com/) as package manager for Python.
I ran

    conda install selenium

and, together with Chrome and ChromeDriver, I was good to go.


## Resources

These should be helpful in case you want to understand my code (I might have used some of these myself...)

- [Selenium: Documentation for Python bindings](https://selenium-python.readthedocs.io/)
- [Stack Overflow: Listing select option values with Selenium and Python](https://stackoverflow.com/questions/18515692/listing-select-option-values-with-selenium-and-python)
- [Stack Overflow: How to select a drop-down menu option value with Selenium (Python)](https://stackoverflow.com/questions/7867537/how-to-select-a-drop-down-menu-option-value-with-selenium-python)
