from requests import *
def htmlurl(url):
	try:
		r=get(url)
		r.raise_for_status()
		r=r.json()
		return(r.keys())
	except:
		print("error")
if __name__=="__main__":
	url="https://api.github.com/search/repositories?q=language:python&sort=stars"
	print(htmlurl(url))

