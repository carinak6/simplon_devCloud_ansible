import psycopg2

class ConnectionBDD_PG:
    def __init__(self):
        #, dbName, user, passwd, host
        #"Établissement de la connexion - Création du curseur"
        try:
            """ "dbname='postgres' user='cary_mck@bdd-elearning' host='bdd-elearning.postgres.database.azure.com' " + \
            "port= 5432 password='sha1491CBA'" """
            #docker run -it --rm postgres psql -h carina-bddscrapping.postgres.database.azure.com -U caryk6@carina-bddscrapping -p 5432 postgres
            
            host = "localhost"
            dbname = "postgres"
            user = "postgres"
            password ='sha1491'

            conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
            self.cnx  = psycopg2.connect(conn_string)
            
            
            print('connexion reussi PostGresql!!!') 
            #self.mycursor = self.cnx.cursor()
            self.echec =0

        except (Exception, psycopg2.Error) as error :
            print("Something went wrong, La connexion avec la base de données a échoué : "+str(error))       
            self.echec =1 
    
    def create_table(self):
        mon_curseur = self.cnx.cursor()
        mon_curseur.execute("CREATE TABLE IF NOT EXISTS MaTable (id SERIAL PRIMARY KEY, titre VARCHAR(250))")
        self.cnx.commit() #valide la transaction
        print('creation reussi MaTable !!!')

        """  a jouter, pour le liverer les recours
        cur.close()
        conn.close()
        print("La connexion PostgreSQL est fermée") """
    
    def incremente(self):

        cursor = self.cnx.cursor()
        cursor.execute('''INSERT INTO MaTable (titre) VALUES ('coucou')''')

        self.cnx.commit()

        return 'Plus +1!!!'
    
    def afficher(self):
        
        try:
            mon_cursor = self.cnx.cursor()

            mon_cursor.execute('''SELECT MAX(id) FROM MaTable''')
            res = mon_cursor.fetchall()
            
            """ self.liste_donnes_offer=[]
            for line in res:
                #print(line)
                self.liste_donnes_offer.append(line) """

            return "L'id en cours est "+str(res[0][0])

        except(Exception, psycopg2.Error) as error:
            print("Something went wrong, un erreur se produit : {}".format(error))
