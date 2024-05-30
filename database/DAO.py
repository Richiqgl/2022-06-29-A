from database.DB_connect import DBConnect
from modello.Album import Album
class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAlbum(numero):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT a.*,COUNT(t.TrackId)as Conteggio 
FROM track t ,album a
WHERE t.AlbumId =a.AlbumId 
GROUP by t.AlbumId 
HAVING COUNT(t.TrackId)>%s 

  """
        cursor.execute(query, (numero,))

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result


if __name__=="__main__":
    print(DAO.getAlbum(18))