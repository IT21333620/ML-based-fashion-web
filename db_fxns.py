# DB
import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

# Functions

def create_item_table():
	c.execute('CREATE TABLE IF NOT EXISTS itemstable(category TEXT,subcategory TEXT,name TEXT,price INTEGER,discount INTEGER,likes INTEGER,isnew TEXT,brand TEXT,colour1 TEXT,colour2 TEXT,photo TEXT)')

def add_item_data(category,subcategory,name,price,discount,likes,isnew,brand,colour1,colour2,photo):
	c.execute('INSERT INTO itemstable(category,subcategory,name,price,discount,likes,isnew,brand,colour1,colour2,photo) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
		   (category,subcategory,name,price,discount,likes,isnew,brand,colour1,colour2,photo))
	conn.commit()

def view_all_inventry_items():
	c.execute('SELECT * FROM itemstable')
	data = c.fetchall()
	return data

def view_unique_item():
    c.execute('SELECT DISTINCT name FROM itemstable')
    data = c.fetchall()
    return data

def get_item(name):
    c.execute('SELECT * FROM itemstable WHERE name = "{}" '.format(name))
    data = c.fetchall()
    return data

def edit_item(newitem_category,newitem_sub_category,newitem_name,newitem_price,newitem_discount,newitem_isnew,newitem_brand,
			  newitem_color_varient_1,newitem_color_varient_2,newitem_image,get_category,get_subcategory,get_name,get_price,
			  get_discount,get_isnew,get_brand,get_colour1,get_colour2,get_url):
    c.execute('UPDATE itemstable SET category=?,subcategory=?,name=?,price=?,discount=?,likes=0,isnew=?,brand=?,colour1=?,colour2=?,photo=?  WHERE category=? AND subcategory=? and name=? AND price=? AND discount=? AND likes=0 AND isnew=? AND brand=? AND colour1=? AND colour2=? and photo=?',
			  (newitem_category,newitem_sub_category,newitem_name,newitem_price,newitem_discount,newitem_isnew,newitem_brand,
			  newitem_color_varient_1,newitem_color_varient_2,newitem_image,get_category,get_subcategory,get_name,get_price,
			  get_discount,get_isnew,get_brand,get_colour1,get_colour2,get_url))
    conn.commit()
    data = c.fetchall()
    return data

def delete_item(name):
	c.execute('DELETE FROM itemstable WHERE name="{}"'.format(name))
	conn.commit()

def get_item_image(name):
    c.execute('SELECT photo FROM itemstable WHERE name = ?', (name,))
    image_url = c.fetchone()
    if image_url:
        return image_url[0]
    else:
        return None

# Login/Signup



def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable (name TEXT, age INTEGER, gender TEXT, username TEXT PRIMARY KEY, password TEXT,usertype TEXT)')


def add_userdata(name,age,gender,username,password,usertype):
	c.execute('INSERT INTO userstable(name,age,gender,username,password,usertype) VALUES (?,?,?,?,?,?)',
		   (name,age,gender,username,password,usertype))
	conn.commit()
	

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def get_user_type(username):
    c.execute('SELECT usertype FROM userstable WHERE username = ?', (username,))
    user_type = c.fetchone()
    if user_type:
        return user_type[0]
    else:
        return None


# Function to create Item rating table

def create_item_rating_table(): 
    cursor = conn.cursor()
    # Define the SQL command to create the item_rating table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS item_rating (
        RatingID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        UserName TEXT,
        ItemName TEXT,
        Rating INTEGER,
        FOREIGN KEY (UserID) REFERENCES userstable (rowid),  -- Assuming userstable has a rowid column
        FOREIGN KEY (UserName) REFERENCES userstable (username) -- Assuming userstable has a username column
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

def save_item_rating(username, item_name, rating):
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    try:
        # Insert the rating into the item_rating table
        cursor.execute("INSERT INTO item_rating (UserID, UserName, ItemName, Rating) VALUES (?, ?, ?, ?)",
                       (get_user_id(username), username, item_name, rating))
        # Commit the changes
        conn.commit()
        return True  # Return True to indicate successful saving of rating
    except Exception as e:
        print(f"Error saving rating: {e}")
        conn.rollback()
        return False  # Return False to indicate an error occurred while saving rating

# Function to get the UserID based on the username
def get_user_id(username):
    c.execute('SELECT rowid FROM userstable WHERE username = ?', (username,))
    user_id = c.fetchone()
    if user_id:
        return user_id[0]
    else:
        return None