from facebook_scraper import get_posts 


class Scraper():
 	
 	
	def scrape_data(self, page_name):
		listposts = []
		for post in get_posts(page_name, pages=1):
			
			item = { 'url_page' : "https://facebook.com/"+page_name+"/",
			'post_id' : post["post_id"],
			'text' : post['text'], 
			'time' : post["time"], 
			'image' : post["image"], 
			'likes' : post["likes"], 
			'comments' : post["comments"], 
			'shares': post["shares"], 
			'reactions' : post["reactions"], 
			'post_url': post["post_url"]}
			
			listposts.append(item)
			
		
		return listposts
		
		   			
    		
