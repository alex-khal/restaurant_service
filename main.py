import DB_singelton
import process_data


if __name__ == '__main__':

    database = DB_singelton.DB_singelton()
    url = 'https://tenbis-static.azureedge.net/restaurant-menu/19156_en'
    data = process_data.load_data(url)









