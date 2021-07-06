# Assessment 2: Sqlite / Pandas Compare
## The Task
Your business partner is interested in using either pandas as sqlite to calculate some statistics on this dataset.  

Set up a sqlite database to do a few comparisons with pandas.  Your business partner is interested in both run time and ease of use. 
    
Don't get too deep - let's just find out which is faster and which is easier to code up.

Do this analysis on the uncorrupted component of the data only.


Compare sqlite vs pandas on the following tasks:

	a) calculate top 25 most common 'makes'
    b) calculate most common 'Color' for each 'Make' 
    c) find the first ticket issued for each 'Make'

Choose either pandas or sqlite to answer the following question:

"Is an out-of-state license plate more likely to be expired at the time of recieving a ticket than an in-state license plate?"

## Results
SQL analysis can be found in `analysis.sql`. Pandas analysis can be found in the `pandas_compare.ipynb` notebook.

### Pandas versus SQLite
#### SQLite
To begin, I setup a quick database (see `sqlite_db_setup.py`). From there, I imported the db into DBeaver and got to work running a few queries. These took very little time to write and they ran in four, five, and ten seconds respectively.

#### Pandas
Tasks a, b, and c took just a second to complete. The code could for each can be written in a single chain (although for ease of reading could also be split up into multiple lines). 

### Comparison
This may be a case of "to each their own". I was able to whip up the SQL rather quickly. But at scale these queries would take longer than building in Pandas. That said, chained Pandas statements can get unweildy and be a bit hard on the eyes. So, depending on my business partner's skillset, I would say that either would be just fine - the setup for SQLite is a bit more involved. But once everything is set up, it is a matter of which language you are more comfortable working.

I was unable to get to the final question due to time constraints (I wanted to get this out the door as quickly as possible). 
