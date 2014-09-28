#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

# model from historical legislator file which is in the following format:
'''
- id:
    bioguide: B000226
    govtrack: 401222
    icpsr: 507
  name:
    first: Richard
    last: Bassett
  bio:
    birthday: '1745-04-02'
    gender: M
  terms:
  - type: sen
    start: '1789-03-04'
    end: '1793-03-02'
    state: DE
    class: 2
    party: Anti-Administration
'''
class Legislator(models.Model):
    # bioguide id  = first letter of last name 
    # and 6 digit number; used for access to 
    # bioguides at congressional biographical directory
    # for instance B000226 would correspnd to 
    # Richard Bassett:
    # http://bioguide.congress.gov/scripts/biodisplay.pl?index=B000226
    bioguide_id = models.CharField(max_length=8, primary_key=True)
    # govtrack_id = 6 digit number used to access
    # information at the govtrack.us website
    # it is redundant in that you also need the person's
    # name if it is a person, so Richard Bassett would be:
    # https://www.govtrack.us/congress/members/richard_bassett/401222
    govtrack_id = models.IntegerField()
    # id for Inter-university Consortium for
    # Political and Social Research
    # not sure how we will use this yet
    icpsr_id = models.IntegerField()
    # for house members only
    house_history_id = models.IntegerField(default=-1)
    thomas_id = models.CharField(max_length=8, default="none")
    opensecrets_id = models.CharField(max_length=16, default=-1)
    votesmart_id = models.IntegerField(default=-1)
    cspan_id = models.IntegerField(default=-1)
    wikipedia_id= models.CharField(max_length=48, default="none")
    ballotpedia_id= models.CharField(max_length=48,default="none")
    maplight_id= models.IntegerField(default=-1)
    washington_post_id= models.CharField(max_length=48, default="none")
    first_name = models.CharField(max_length=32)
    last_name  = models.CharField(max_length=32)
    bio_birthday = models.DateField()
    bio_gender = models.CharField(max_length=1)

class Terms(models.Model):
    bioguide_id = models.ForeignKey(Legislator)
    terms_type = models.CharField(max_length=8)
    terms_start = models.DateField()
    terms_end = models.DateField()
    terms_state = models.CharField(max_length=2)
    terms_class  = models.IntegerField(default=-1)
    terms_party = models.CharField(max_length=32)
    terms_district = models.IntegerField(default=-1)


