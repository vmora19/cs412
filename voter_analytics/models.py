from django.db import models

# Create your models here.

class Voter(models.Model):
    '''
    Store/represent the data from one voter in the town of Newton, MA
    Voter ID Number, Last Name, First Name, Street Number, Street Name, 
    Apartment Number, Zip code, DOB, Date of Registration, Party Affiliation,
    Precinct Number, v20state, v21town, v21primary, v22general, v23town, voter_score
    '''

    #identification
    voter_id = models.TextField()
    last_name = models.TextField()
    first_name = models.TextField()
    street_num = models.IntegerField()
    street_name = models.TextField()
    apt_num = models.IntegerField()
    zip = models.IntegerField()
    dob = models.TextField()
    date_registration = models.TextField()
    party = models.TextField()
    precinct = models.IntegerField()

    #voting info
    v20 = models.TextField()
    v21town = models.TextField()
    v21primary = models.TextField()
    v22 = models.TextField()
    v23 = models.TextField()
    voter_score = models.TextField()

    def __str__(self):
        '''Return a string representation of this model instance.'''
        return f'{self.first_name} {self.last_name} ({self.voter_id}, {self.dob}), {self.voter_score}'
    
def load_data():
    '''Function to load data records from CSV file into Django model instances.'''


    filename = '/Users/valentina/Desktop/newton_voters.csv'
    f = open(filename)
    f.readline() # discard headers

    for line in f:
        fields = line.split(',')
       
        try:
            # create a new instance of Result object with this record from CSV
            voter = Voter(voter_id=fields[0],
                            last_name=fields[1],
                            first_name=fields[2],
                            street_num = fields[3],
                            street_name = fields[4],
                            apt_num = fields[5],
                            zip = fields[6],
                            dob = fields[7],
                            date_registration = fields[8],
                            party = fields[9],
                            precinct = fields[10],
                        
                            v20 = fields[11],
                            v21town = fields[12],
                            v21primary = fields[13],
                            v22 = fields[14],
                            v23 = fields[15],
                            voter_score = fields[16],
                        )
        
 
 
            voter.save() # commit to database
            print(f'Created result: {voter}')
            
        except:
            print(f"Skipped: {fields}")
    
    print(f'Done. Created {len(Voter.objects.all())} Voters.')