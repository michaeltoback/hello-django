import requests
import json
from yaml import load, dump
from datetime import datetime
from hello.models import Legislator, Terms
'''
bulkload data in the following format:
{'bio': {'gender': 'M', 'birthday': '1745-04-02'}, 'terms': [{'start': '1789-03-04', 'state': 'DE', 'end': '1793-03-02', 'party': 'Anti-Administration', 'type': 'sen', 'class': 2}], 'id': {'bioguide': 'B000226', 'govtrack': 401222, 'icpsr': 507}, 'name': {'last': 'Bassett', 'first': 'Richard'}}

Note that the format in the database is the combination of the key and subkey
so bio_gender, terms_start, etc.

the model:
class legislator(models.Model):
    # bioguide id  = first letter of last name
    # and 6 digit number; used for access to
    # bioguides at congressional biographical directory
    # for instance B000226 would correspnd to
    # Richard Bassett:
    # http://bioguide.congress.gov/scripts/biodisplay.pl?index=B000226
    bioguide_id = models.CharField(max_length=8. primary_key=True)
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
    first_name = models.CharField(max_length=32)
    last_name  = models.CharField(max_length=32)
    bio_birthday = models.DateField()
    bio_gender = models.CharField(max_length=1)
    terms_type = models.CharField(max_length=8)
    terms_start = models.DateField()
    terms_end = models.DateField()
    terms_state = models.CharField(max_length=2)
    terms_class  = models.IntegerField(default=-1)
    terms_party = models.CharField(max_length=32)
    terms_district = models.IntegerField(default=-1)
'''
def main():
    data = open("legislators-historical.yaml","r")
    start_yaml = True
    for line in data:
        print "next line:" + line
        if line[0] != "-":
            str += line
            print "not the start so appending this line"
            continue

        elif start_yaml:
            print "starting a new yaml"
            str = line 
            start_yaml = False
            continue            
        print str          
        yaml_sets = load(str)
        for yaml_set in yaml_sets:
            if 'bio' in yaml_set:
                bio = yaml_set['bio'] 
                if 'gender' in bio:
                    bio_gender = bio['gender']
                else:
                     bio_gender = 'M' # really?? yes I've seen this
                if 'birthday' in bio:
                    bio_birthday = datetime.strptime(bio['birthday'], "%Y-%m-%d").date()          
                else:
                    bio_birthday = datetime.strptime("1600-01-01", "%Y-%m-%d").date()
            else:
                bio_gender = 'M'
                bio_birthday =  datetime.strptime("1600-01-01", "%Y-%m-%d").date()
            id = yaml_set['id']
            id_bioguide = id['bioguide']
            id_govtrack = id['govtrack']
            if 'icpsr' in id:
                id_icpsr = id['icpsr']
            else:
                id_icpsr = 0
            if 'house_history' in id:
                id_house_history = id['house_history']
            else:
                id_house_history = 0
            if 'thomas' in id:
                thomas_id = id['thomas']
            else:
                thomas_id = 'none'
            if 'opensecrets' in id:
                opensecrets_id = id['opensecrets']
            else:
                opensecrets_id = "none"
            if 'votesmart' in id:
                votesmart_id = id['votesmart']
            else:
                votesmart_id = 0
            if 'cspan' in id:
                cspan_id = id['cspan']
            else:
                cspan_id = 0
            if 'wikipedia' in id:
                wikipedia_id = id['wikipedia']
            else:
                wikipedia_id = yaml_set['name']['first'] + " " + yaml_set['name']['last']
            if 'ballotpedia' in id:
                ballotpedia_id = id['ballotpedia']
            else:
                ballotpedia_id = "none"
            if 'maplight' in id:
                maplight_id = id['maplight']
            else:
                maplight_id = 0
            if 'washington_post' in id:
                washington_post_id = id['washington_post']
            else:
                washington_post_id = "none"
            name = yaml_set['name']
            first_name = name['first']
            last_name = name['last']
            y1= Legislator.objects.create(
            bioguide_id=id_bioguide,
            govtrack_id=id_govtrack,
            icpsr_id=id_icpsr,
            house_history_id=id_house_history,
            thomas_id=thomas_id,
            opensecrets_id=opensecrets_id,
            votesmart_id=votesmart_id,
            cspan_id=cspan_id,
            wikipedia_id=wikipedia_id,
            ballotpedia_id=ballotpedia_id,
            maplight_id=maplight_id,
            washington_post_id=washington_post_id,
            first_name=first_name,
            last_name=last_name,
            bio_birthday=bio_birthday,
            bio_gender=bio_gender)
            y1.save()
            terms = yaml_set['terms']
            for term in terms:
                terms_start = datetime.strptime(term['start'], "%Y-%m-%d").date()
                if 'state' in term:
                     terms_state = term['state']
                else:
                     terms_state = "  "
                terms_end = datetime.strptime(term['end'], "%Y-%m-%d").date()
                if 'party' in term:
                    terms_party = term['party']
                else:
                    terms_party = 'Unknown'
                terms_type = term['type']
                if 'class' in term:
                    terms_class = term['class']
                else:
                    terms_class = 0
                if 'district' in term:
                    terms_district = term['district']
                else:
                    terms_district = 0
                t1= Terms.objects.create(bioguide_id=y1,
                    terms_type=terms_type,
                    terms_start=terms_start,
                    terms_end=terms_end,
                    terms_state=terms_state,
                    terms_class=terms_class,
                    terms_party=terms_party,
                    terms_district=terms_district)
                t1.save()
        str = line
    if len(str) > 0:
        yaml_sets = load(str)
        for yaml_set in yaml_sets:
            if 'bio' in yaml_set:
                bio = yaml_set['bio']
                if 'gender' in bio:
                    bio_gender = bio['gender']
                else:
                     bio_gender = 'M' # really?? yes I've seen this
                if 'birthday' in bio:
                    bio_birthday = datetime.strptime(bio['birthday'], "%Y-%m-%d").date()
                else:
                    bio_birthday = datetime.strptime("1600-01-01", "%Y-%m-%d").date()
            else:
                bio_gender = 'M'
                bio_birthday =  datetime.strptime("1600-01-01", "%Y-%m-%d").date()
            id = yaml_set['id']
            id_bioguide = id['bioguide']
            id_govtrack = id['govtrack']
            if 'icpsr' in id:
                id_icpsr = id['icpsr']
            else:
                id_icpsr = 0
            if 'house_history' in id:
                id_house_history = id['house_history']
            else:
                id_house_history = 0
            name = yaml_set['name']
            first_name = name['first']
            last_name = name['last']
            y1= Legislator.objects.create(
            bioguide_id=id_bioguide,
            govtrack_id=id_govtrack,
            icpsr_id=id_icpsr,
            house_history_id=id_house_history,
            first_name=first_name,
            last_name=last_name,
            bio_birthday=bio_birthday,
            bio_gender=bio_gender)
            y1.save()
            terms = yaml_set['terms']
            for term in terms:
                terms_start = datetime.strptime(term['start'], "%Y-%m-%d").date()
                if 'state' in term:
                     terms_state = term['state']
                else:
                     terms_state = "  "
                terms_end = datetime.strptime(term['end'], "%Y-%m-%d").date()
                if 'party' in term:
                    terms_party = term['party']
                else:
                    terms_party = 'Unknown'
                terms_type = term['type']
                if 'class' in term:
                    terms_class = term['class']
                else:
                    terms_class = 0
                if 'district' in term:
                    terms_district = term['district']
                else:
                    terms_district = 0
                t1= Terms.objects.create(bioguide_id=y1,
                    terms_type=terms_type,
                    terms_start=terms_start,
                    terms_end=terms_end,
                    terms_state=terms_state,
                    terms_class=terms_class,
                    terms_party=terms_party,
                    terms_district=terms_district)
                t1.save()
 
if __name__ == "__main__":
    main()
