for offset in range(0,5963000,1000):
    req='https://api.vk.com/method/groups.getMembers?group_id=%s&offset=%d&access_token=%s'%(group,offset,vkapi.access_token)
    print "~~~~~~~~~~~" + str(offset)
    try:
        f=urllib2.urlopen(req)
    except:
        "something wrong with offset"
    profiles=json.loads(f.read().decode("utf-8"))
    profiles=[item for item in profiles['response']['users']]
    for user in profiles:
        req='https://api.vk.com/method/wall.get?owner_id=%s&filter=owner&count=%d&access_token=%s'%(user,1,vkapi.access_token)
        try:
            f=urllib2.urlopen(req)
        except:
            "Something wrong with user"
        sleep(0.3)
        post=json.loads(f.read().decode("utf-8"))
        try:
            post=post['response'][1]['id']
            print ("wall%s_%s")%(user, post)
            req='https://api.vk.com/method/wall.repost?object=wall%s_%s&group_id=%d&access_token=%s'%(user,post,83719092,vkapi.access_token)
            try:
                f=urllib2.urlopen(req)
            except:
                "Something wrong with repost"
            sleep(0.3)
            try:
                repost=json.loads(f.read().decode("utf-8"))
                if repost.get('error') and repost['error'].get('captcha_img'):
                    with open('captcha.jpeg', 'wb') as outfile:
                        outfile.write(urllib2.urlopen(repost['error']['captcha_img']).read())
                    outfile.close()
                    sleep(0.1)
                    gate = AntiGate('ff3944c2490ee6dcf8872ee03d2a94f6', 'captcha.jpeg')
                    req='https://api.vk.com/method/wall.repost?object=wall%s_%s&group_id=%d&access_token=%s&captcha_sid=%s&captcha_key=%s'%(user,post,83719092,vkapi.access_token,repost['error']['captcha_sid'],gate)
                    try:
                        f=urllib2.urlopen(req)
                        print json.loads(f.read().decode("utf-8"))
                    except:
                        "Something wrong with repost"
                print repost
                print "user: %s, reposted"%user
            except:
                print f.read()


        except Exception,e:
            print post