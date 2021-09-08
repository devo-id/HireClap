import sqlite3

#create database and connects or connects to database if database already exists
conn = sqlite3.connect('Database.db')
cur = conn.cursor()

# create table if not exists
def createTable():
    cur.execute(""" CREATE TABLE  IF NOT EXISTS  Movies (
                                        movieName text,
                                        leadActor text,
                                        actress text,
                                        yearOfRelease integer,
                                        directorName text
                                    ); """)
               
#Inserting data into the table 
def dataEntry():
    cur.execute("INSERT INTO Movies VALUES('Star Trek','J.J. Abrams','Simon Pegg','2009','Robert Aldrich')")
    cur.execute("INSERT INTO Movies VALUES('The Gun',' Robert De Niro','Scarlett Johansson','2001','Pedro Almodóvar')")
    cur.execute("INSERT INTO Movies VALUES('Bottle Rocket ','Jack Nicholson','Anne Hathaway','1998','Woody Allen')")
    cur.execute("INSERT INTO Movies VALUES('Rushmore ','Marlon Brando','Natalie Portman','1990','Robert Altman')")
    cur.execute("INSERT INTO Movies VALUES('Apur Sansar','Denzel Washington','Margot Robbie','2002','Satyajit Ray')")
    cur.execute("INSERT INTO Movies VALUES('McCabe & Mrs. Miller','Humphrey Bogart','Emily Blunt','2007','Wes Anderson')")
    cur.execute("INSERT INTO Movies VALUES('The Long Goodbye','Sidney Poitier','Jessica Alba','2018','Michelangelo Antonioni')")
    cur.execute("INSERT INTO Movies VALUES('All About My Mother','Clark Gable','Brie Larson','2011','John G. Avildsen')")
    cur.execute("INSERT INTO Movies VALUES('Volver','Tom Hanks','Lea Seydoux','1997','John Badham')")
    cur.execute("INSERT INTO Movies VALUES('Broken Embraces','Gregory Peck','Rachel McAdams','1998','Noah Baumbach')")
    cur.execute("INSERT INTO Movies VALUES('Love and Death','Leonardo DiCaprio','Ellen Pompeo','1987','James Cameron')")
    cur.execute("INSERT INTO Movies VALUES('California Suite','Spencer Tracy','Mila Kunis','1986','Leos Carax')")
    conn.commit()
    conn.close()

# function to query all rows from the table
def queryAll():
    cur.execute("SELECT * from Movies;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

# function to call rows depending upon passed value
def query(actorName):
    cur.execute("SELECT * from Movies WHERE leadActor=?",(actorName,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
# call funtion whem required
    # createTable()
    # dataEntry()
    # queryAll()        
    actorName = input("Actor Name:")
    query(actorName)
        
    
if __name__ == '__main__':
    main()