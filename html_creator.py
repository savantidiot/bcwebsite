from contentmanagement import Content

TOPIC_DICT = Content()

FUNC_TEMPLATE = '''

@app.route("CURRENTROUTE", methods=['GET', 'POST'])
def CURRENTTITLE():
    return render_template("/CURRENTTOPIC/CURRENTHTML", post_date = TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][0], post_title = TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1], post_url = TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][2], user_name = user_name)

'''

for each_topic in TOPIC_DICT:
    #print(each_topic)

    index_counter = 0
    for eachele in TOPIC_DICT[each_topic]:
        try:
            CURRENTHTML = (eachele[2]+'.html').replace("/","")
            CURRENTROUTE = ('/'+each_topic+'/'+eachele[2])
            CURRENTTOPIC = each_topic
            CURRENTTITLE = eachele[1].replace("-","_").replace(" ","_").replace(",","").replace("/","").replace(")","").replace("(","").replace(".","").replace("!","").replace(":","-").replace("'","")
            CURRENTINDEX = str(index_counter)
            NEXTINDEX = str(index_counter + 1)
            index_counter += 1

            print( FUNC_TEMPLATE.replace("CURRENTTOPIC",CURRENTTOPIC).replace("CURRENTINDEX",CURRENTINDEX).replace("CURRENTTITLE",CURRENTTITLE).replace("CURRENTHTML",CURRENTHTML).replace("NEXTINDEX",NEXTINDEX).replace("CURRENTROUTE",CURRENTROUTE) )

        except Exception as e:
            print(str(e))