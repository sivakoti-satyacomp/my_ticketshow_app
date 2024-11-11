from flask_restful import Resource, Api
from flask import request
from .models import *
from datetime import datetime


api=Api()

class ShowApi(Resource):

    #Reading of data
    def get(self):
        shows=Show.query.all()
        shows_json=[]
        for show in shows:
            shows_json.append({'id':show.id,'name':show.name,'tags':show.tags,'overall_rating':show.rating, 'tkt_price':show.tkt_price,'date_time':str(show.date_time),'theatre_id':show.theatre_id})
        
        return shows_json
    
    #Creating data
    def post(self):
        name=request.json.get("name")
        tags=request.json.get("tags")
        rating=request.json.get("overall_rating")
        tkt_price=request.json.get("tkt_price")
        date_time=request.json.get("date_time")
        theatre_id=request.json.get("theatre_id")
        dt_time=datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S")
        new_show=Show(name=name,tags=tags,rating=rating,tkt_price=tkt_price,date_time=dt_time,theatre_id=theatre_id)
        db.session.add(new_show)
        db.session.commit()
        
        return {"message":"New show added!"},201
    

    #Updating
    def put(self,id):
        show=Show.query.filter_by(id=id).first()
        if show:
            show.name=request.json.get("name")
            show.tags=request.json.get("tags")
            show.rating=request.json.get("overall_rating")
            show.tkt_price=request.json.get("tkt_price")
            date_time=request.json.get("date_time")
            dt_time=datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S")
            show.date_time=dt_time
            show.theatre_id=request.json.get("theatre_id")
            db.session.commit()
            return {"message":"Show updated!"},200
        
        return {"message":"Show id not found!"},404

    #Delete data
    def delete(self,id):
        show=Show.query.filter_by(id=id).first()
        if show:
            db.session.delete(show)
            db.session.commit()
            return {"message":"Show deleted!"},200
        
        return {"message":"Show id not found!"},404

class ShowSearchApi(Resource):
    def get(self,id):
        show=Show.query.filter_by(id=id).first()
        if show:
            shows_json=[]
            shows_json.append({'id':show.id,'name':show.name,'tags':show.tags,'overall_rating':show.rating, 'tkt_price':show.tkt_price,'date_time':str(show.date_time),'theatre_id':show.theatre_id})
            return shows_json
        return {"message":"Show id not found!"},404

api.add_resource(ShowApi,"/api/get_shows","/api/add_show","/api/edit_show/<id>","/api/delete_show/<id>")
api.add_resource(ShowSearchApi,"/api/search_show/<id>")