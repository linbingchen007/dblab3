# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Variable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15,blank=True,db_index=True)
    val = models.CharField(max_length=50,default='')

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25,blank=True)
    password = models.CharField(max_length=25,blank=True)
    email = models.CharField(max_length=75,blank=True)
    balance = models.IntegerField(default=0)

class Promo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,related_name='promo')
    invites = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)




class Ip(models.Model):  # Many to one Ip -- User
    id = models.AutoField(primary_key=True)
    ipaddr = models.CharField(max_length=25)
    reged = models.BooleanField(default=False)
    p_user = models.ForeignKey(User)



class Film(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    covurl = models.CharField(max_length=100,default="")

class Film_User_Favrel(models.Model):
    id = models.AutoField(primary_key=True)
    fid = models.IntegerField(db_index=True,blank=True)
    uid = models.IntegerField(db_index=True,blank=True)

class Film_User_Ownrel(models.Model):
    id = models.AutoField(primary_key=True)
    fid = models.IntegerField(db_index=True,blank=True)
    uid = models.IntegerField(db_index=True,blank=True)

class Tag(models.Model):  # Many to many  Tag -- Film
    id = models.AutoField(primary_key=True)
    tagname = models.CharField(max_length=30,blank=True)


class Tag_Film_Rel(models.Model):
    id = models.AutoField(primary_key=True)
    fid = models.IntegerField(db_index=True,blank=True)
    tid = models.IntegerField(db_index=True,blank=True)

class Category_Film_Rel(models.Model):
    id = models.AutoField(primary_key=True)
    fid = models.IntegerField(db_index=True,blank=True)
    cid = models.IntegerField(db_index=True,blank=True)


class Category(models.Model):  # Many to many  Category -- Film
    id = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=40,blank=True)


class Pic(models.Model):  # Many to one Pic -- Film
    id = models.AutoField(primary_key=True)
    picurl = models.CharField(max_length=100,blank=True)
    film = models.ForeignKey(Film)


class Vid(models.Model):
    id = models.AutoField(primary_key=True)
    vidurl = models.CharField(max_length=100,blank=True)
    film = models.ForeignKey(Film)
