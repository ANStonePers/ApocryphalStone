import glob, requests, os, pickle, time
from bs4 import BeautifulSoup

ALREADY_DOWNLOADED_PDFS = True
ALREADY_WRITTEN_HTMLS = True

def create_empty_file(path: str) -> None:
    """
    Creates a new empty file at the specified path.
    All intermediate directories will also be created if they do not exist.

    :param path: The full file path (including directories) for the new file.
    """
    # Ensure the directory exists
    directory = os.path.dirname(path)
    if directory:  # This checks to avoid issues if path is just a filename without directories
        os.makedirs(directory, exist_ok=True)

    # Create the empty file
    with open(path, 'w'):
        pass

# Change this pattern to match your actual filename structure.
# For example, if your files are named "report1.html", "report2.html", etc.
pattern = "bib_ps/bib_p*.html"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

# Use glob to find all matching files in the current directory
matching_files = glob.glob(pattern)

site_url_to_pdf = {}
site_url_to_doc_title = {}

if os.path.exists("./cached_obj/sutp.obj"):
    with open("./cached_obj/sutp.obj", "rb") as file:
        site_url_to_pdf = pickle.load(file)
    with open("./cached_obj/dt.obj", "rb") as file:
        site_url_to_doc_title = pickle.load(file)
else:
    for filename in matching_files:
        print(f"Parsing file: {filename}")
        with open(filename, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

            ul = soup.find("ul", { "class": "unstyled main-items" })

            # Example: Find and print the title of each HTML page (if available)
            lis = ul.find_all('li')

            for li in lis:
                a_ = li.find("a")
                dt = a_.get_text()
                url = a_['href']
                if url[0] == "/":
                    print(url)
                    full_url = f"http://apocryphalstone.com{url}"
                    sp = BeautifulSoup(requests.get(full_url, headers=headers).content, 'html.parser')
                    embed = sp.find("iframe")
                    orig_url = embed['src']
                    print(orig_url)
                    site_url_to_pdf[url] = orig_url
                    site_url_to_doc_title[url] = dt
    with open("./cached_obj/sutp.obj", "wb") as file:
        pickle.dump(site_url_to_pdf, file)
    with open("./cached_obj/dt.obj", "wb") as file:
        pickle.dump(site_url_to_doc_title, file)

if not ALREADY_DOWNLOADED_PDFS:
    for k, v in site_url_to_pdf.items():
        full_u = f"http://apocryphalstone.com{v}"
        print(full_u)

        if v.strip() == "": continue

        create_empty_file(f'./to_copy{v}')
        with open(f"./to_copy{v}", "wb") as file:
            file.write(requests.get(full_u, headers=headers).content)

if not ALREADY_WRITTEN_HTMLS:
    for k, v in site_url_to_pdf.items():
        full_u = f"http://apocryphalstone.com{v}"
        print(full_u)

        if v.strip() == "": continue
        
        doc_title = site_url_to_doc_title[k]

        create_empty_file(f'./to_copy{k}.html')
        time.sleep(0.5)
        with open(f"./to_copy{k}.html", "wb") as file:
            file.write(("""
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="language" content="en" />
        
    
            
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="/ApocryphalStone/assets/css/extra.css" />
    <script type="text/javascript" src="/ApocryphalStone/assets/js/extra.js"></script>
    <title>Michael E. Stone</title>
    </head>

    <body>
    <div class="container-fluid">
    <div class="container-narrow shadow">
        <header>
            <div class="row-fluid">
            <div class="navbar navbar-inverse"><div class="navbar-inner"><div class="container"><a href="/ApocryphalStone" class="brand"><img src="/ApocryphalStone/assets/images/logo.png" alt="Michael E. Stone, Ph. D." /></a></div></div></div>    	</div>
            <div class="row-fluid header-image"></div>
            <div class="row-fluid">
            <div class="navbar navbar-inverse"><div class="navbar-inner"><div class="container"><a href="/ApocryphalStone" class="brand"></a><ul id="yw2" class="nav"><li><a href="/ApocryphalStone">Home</a></li><li><a href="/ApocryphalStone/bibliography">Bibliography</a></li><li><a href="/ApocryphalStone/poetry">Poetry</a></li><li><a href="/ApocryphalStone/links">Useful Links</a></li><li><a href="/ApocryphalStone/contact">Contact</a></li><li><a href="/ApocryphalStone/news">News</a></li><li><a href="/ApocryphalStone/familytree">Family Site</a></li></ul></div></div></div>        </div>
        </header>

                    

                    <div class="row-fluid maincontent">
            <div class="">
                <div class="center">
        <div class="left">
        <a class="btn btn-inverse btn-large" id="yw0" href="/ApocryphalStone/bibliography" ><i class="icon-arrow-left"></i> Back</a>    </div>

        <h4>Bibliography - """+doc_title+"""</h4>
        <div>
            <iframe src="/ApocryphalStone"""+v+"""" type="application/pdf" width="100%" height="700px">
                <p>Sorry. It appears your browser cannot disaply this PDF file.</p>
                <p>You can download it <a href="/ApocryphalStone"""+v+'''">here</a> instead.</p>
            </iframe>
        </div>
    </div>

    <div>

    </div>      	</div>
        </div>


        <div class="footer">
            Copyright &copy; 2025 Michael E. Stone.<br/>
            All Rights Reserved.<br/>
            Powered by <a href="http://www.yiiframework.com/" rel="external">Yii Framework</a>.      </div>

        </div> <!-- /container -->
    </div>

    <script type="text/javascript" src="/assets/d51b8ad/listview/jquery.yiilistview.js"></script>
    <script type="text/javascript">
    /*<![CDATA[*/
    jQuery(function($) {
    jQuery('a[rel="tooltip"]').tooltip();
    jQuery('a[rel="popover"]').popover();
    jQuery('#yw0').yiiListView({'ajaxUpdate':['yw0'],'ajaxVar':'ajax','pagerClass':'pagination','loadingClass':'list-view-loading','sorterClass':'sorter','enableHistory':false,'afterAjaxUpdate':function() {
                jQuery('.popover').remove();
                jQuery('a[rel="popover"]').popover();
                jQuery('.tooltip').remove();
                jQuery('a[rel="tooltip"]').tooltip();
            }});
    });
    /*]]>*/
    </script>
    </body>
    </html>
    ''').encode('utf-8'))

for k, v in site_url_to_pdf.items():
    print(f'- {k.split("/")[-1]}: {k.split("/")[-1]}.html')