import sqlite3
PATH_DB = "C:/DEV/PillData/Sqlite_DB/pills_5_filtered.db"
SIZE_TOLERANCE = 1 # margin of error of pill size (in milimeters)


def query_pills(pill_properties):
    """
    Queries pill information from DB
    Query is constructed dynamically, input values are checked
    to avoid SQL injection
    Input format:
    {"imprints": [], "colors": [], "shape": [], "size": "x"}
    """

    imprint_part_list = pill_properties.get("imprints")
    if imprint_part_list is None:
        print("Imprints not provided")
        return None

    query = "SELECT * FROM pills WHERE 1=1"
    for imprint in imprint_part_list:
        if not imprint.isalnum():
            print("Non alphanumeric value in imprint list")
            return None
        query += f" AND imprint LIKE '%{imprint}%'"

    color_list = pill_properties.get("colors")
    if color_list is not None:
        for color in color_list:
            if not color.isalnum():
                print("Non alphanumeric value in color list")
                return None      
        color_string = ', '.join("'" + item + "'" for item in color_list)
        query += f" AND color IN ({color_string})"

    shape_list = pill_properties.get("shape")
    if shape_list is not None:
        for shape in shape_list:
            if not shape.isalnum():
                print("Non alphanumeric value in shape list")
                return None      
        shape_string = ', '.join("'" + item + "'" for item in shape_list)
        query += f" AND shape IN ({shape_string})"

    size = pill_properties.get("size")
    if size is not None:
        if not size.isnumeric():
                print("Non numeric value in size value")
                return None  
        query += f" AND size >= {int(size) - SIZE_TOLERANCE}"       
        query += f" AND size <= {int(size) + SIZE_TOLERANCE}"       

    print(query)

    conn = sqlite3.connect(PATH_DB)
    c = conn.cursor()
    c.execute(query)
    result = c.fetchall()
    c.close()
    return(result)


# 
pill_1 = {
    "imprints": ["B", "IN"]
  , "colors": ["YELLOW", "ORANGE"]
  , "shape": ["OVAL", "ROUND"]
  , "size": "12"
}


for record in query_pills(pill_1):
    print("----")
    print(record)
    # print(f"name={record[1]}; imprint={record[2]}; code={record[0]}")


# Possible shapes:
# BULLET
# CAPSULE
# CLOVER
# DIAMOND
# DOUBLE CIRCLE
# FREEFORM
# HEXAGON (6 SIDED)
# OCTAGON (8 SIDED)
# OVAL
# PENTAGON (5 SIDED)
# RECTANGLE
# ROUND
# SEMI-CIRCLE
# SQUARE
# TEAR
# TRAPEZOID
# TRIANGLE

# Possible colors:
# BLACK
# BLUE
# BROWN
# GRAY
# GREEN
# ORANGE
# PINK
# PURPLE
# RED
# TURQUOISE
# WHITE
# YELLOW
