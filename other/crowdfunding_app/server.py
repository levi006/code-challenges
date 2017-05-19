from jinja2 import StrictUndefined
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import json
import requests
import re

app = Flask(__name__)
app.secret_key = "indiegogo"

url = "https://api.indiegogo.com/1/campaigns.json?api_token=e377270bf1e9121da34cb6dff0e8af52a03296766a8e955c19f62f593651b346"
response = requests.get(url)

@app.route("/")
def campaign_index():
	"""Homepage--displays all campaigns"""
	data = response.json()

	return render_template("homepage.html", data=data)

@app.route("/search")
def campaign_search():
	"""Displays search results"""
	data = response.json()
	title_input = str(request.args.get("title-search")).rstrip() 
	# print "This is the title input: " + title_input
	tagline_input = str(request.args.get("tagline-search")).rstrip()
	# print "This is the tagline input: " + tagline_input

	search_results = []

	if title_input == "" and tagline_input != "":
		tagline_input_stripped = re.sub('[^a-z\ \']+', " ", tagline_input.lower())
		for campaigns in data['response']:
			campaign_tagline = campaigns['tagline'].lower()
			# print "this is campaign_tagline: " + campaign_tagline
			campaign_tagline_stripped =re.sub('[^a-z\ \']+', " ", campaign_tagline)
			# print "this is campaign tagline stripped again: " + campaign_tagline_stripped
			if tagline_input_stripped in campaign_tagline_stripped:
			    search_results.append(campaigns)

	elif title_input != "" and tagline_input == "":
		title_input_stripped = re.sub('[^a-z\ \']+', " ", title_input.lower())
		for campaigns in data['response']:
			campaign_title = campaigns['title'].lower()
			# print "this is campaign_title: " + campaign_title
			campaign_title_stripped =re.sub('[^a-z\ \']+', " ", campaign_title)
			# print "this is campaign title stripped again: " + campaign_title_stripped
			if title_input_stripped in campaign_title_stripped:
			    search_results.append(campaigns)
	else:
		search_results = data['response']

	data['response'] = search_results
	# print "This is the search result:" + str(len(search_results))

	#if there are no matches
	if  len(search_results) == 0:
		return render_template("sadpanda.html")

	return render_template("search.html", data=data)

if __name__ == "__main__":

    app.debug = False

    DebugToolbarExtension(app)

    app.run()