
import facebook, requests,json, time

token = "EAACEdEose0cBAOjRAvpTAgU1l9Vhp6FgJkxHG99Evhyak7opF6a6mN3qac7eyBC4kVTAn2HmwtYruSvNZCCfxjWXoiUZCDGMSTHZCGz7isrmux6fNZA6ZCIvvZA1hZBHhpG4koEIYTZAq5hTdVjGNrnSRef05TIB5F98YlgIx11BTB3xyZCAeIvd9ZCmPpEATAZCWbhRruMBMtPK8mKVceqX2Sat6mUxvRDeZC0ZD"
me ="111859749635183"
graph = facebook.GraphAPI(access_token=token, version="2.12")

#graph.put_object(parent_object=me, connection_name='feed',
 #                 message='O mundo é um moinho!')
for i in range(10):
	url = requests.get("https://www.vagalume.com.br/news/index.js")
	texto = json.loads(url.text)

	notic = texto["news"][0]["kicker"]
	link = texto["news"][0]["url"]
	ima = texto["news"][0]["pic_src"]
	foto = open("foto.jpg","wb")
	sfoto = requests.get(ima)
	foto.write(sfoto.content)
	foto.close

	graph.put_photo(image=open('foto.jpg', 'rb'),
                message=notic+" "+link)
	time.sleep(108000)

