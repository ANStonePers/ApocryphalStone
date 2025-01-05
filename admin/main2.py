import requests, os, pickle
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

for i in range(2, 7):
    u = f"http://apocryphalstone.com/bibliography/index/ajax/yw0/Bibliography_page/{i}"
    c = requests.get(u, headers=headers).content
    d = BeautifulSoup(c, 'html.parser').find("div", {"class": "row-fluid maincontent"})
    s = str(d)
    with open(f"./to_copy/bibliography/index/Bibliograph_page/{i}.html", "wb") as file:
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
	</header>"""+s+"""

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
""").encode())