 # Xpaths of elements to work with
#from grp import struct_group
from curses import flash
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
from time import sleep 
import json
import re

def read_atributes(repo_url):

    secs_to_wait = 5

    ##github url von vue
    #github_vue_url = "https://github.com/search?l=JavaScript&q=online+shop+vue&type=Repositories" 

    #github_vue_url= "https://github.com/BosNaufal/vue-mini-shop"
    ## css selector of element that we need.
    code_button_selector = '#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > span > get-repo > feature-callout > details > summary'
    linktorepo_selector = '<input type="text" class="form-control input-monospace input-sm color-bg-subtle" data-autoselect="" value="https://github.com/ParniyanSHokoohi/code-quality-web.git" aria-label="https://github.com/ParniyanSHokoohi/code-quality-web.git" readonly="">'
    linktorepo_attribute_value ='value'
    #text= ['strars','Forks','commit','collabration','watching','branches','issues','pull requests','contributors'
    watch_fork_star_selctor ="#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-sidebar > div > div.BorderGrid-row.hide-sm.hide-md > div"
    n_commits_selector ="#repo-content-pjax-container > div.clearfix.container-xl.px-3.px-md-4.px-lg-5.mt-4 > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.Box.mb-3 > div.Box-header.position-relative > div > div:nth-child(4) > ul > li > a > span"
    n_issues_selector ="#issues-tab"
    n_breanches_selector= "#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-main > div.file-navigation.mb-3.d-flex.flex-items-start > div.flex-self-center.ml-3.flex-self-stretch.d-none.d-lg-flex.flex-items-center.lh-condensed-ultra"
    n_pullrequests_selector = '#pull-requests-tab'
    n_contributors_selector = "#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-sidebar > div > div:nth-child(5) > div > h2 > a"



    # Start the browser
    options = Options()
    # set headless option to True to run browser in headless mode
    # options.headless = True


    browser = webdriver.Chrome(options=options)

    

    # Go to the github_vue website
    browser.get(repo_url)### get url github_vue webseite
    browser.set_window_size(1920, 1080)
    browser.maximize_window()
    sleep(secs_to_wait*10)# mach eine Pause.## wir machen pause weil normale mensh mach pause sonst ohne Pause sie merken das ist eine Robat ist.

    try:
        #find elemet watch-folk
        star_watch_folk_element = browser.find_element(By.CSS_SELECTOR, watch_fork_star_selctor)
        watch_folk_text = star_watch_folk_element.get_attribute('textContent')
        #print(watch_folk_text)
    except Exception as e:
        watch_folk_text=''
        print(e)
    
    try:
        n_commits_element = browser.find_element(By.CSS_SELECTOR,n_commits_selector)
        n_commits_text = n_commits_element.get_attribute('textContent')
        #print(n_commits_text)
    except Exception as e:
        print(e)
        n_commits_text=''
    try:
        n_issues_element = browser.find_element(By.CSS_SELECTOR,n_issues_selector)
        n_issues_text = n_issues_element.get_attribute('textContent')
    except Exception as e:
        print(e)
        n_issues_text=''
    try:
        n_breanches_element = browser.find_element(By.CSS_SELECTOR,n_breanches_selector)
        n_breanches_text = n_breanches_element.get_attribute('textContent')
    except Exception as e:
        print(e)
        n_breanches_text=''
    try:
        n_pullrequests_element = browser.find_element(By.CSS_SELECTOR,n_pullrequests_selector)
        n_pullrequests_text = n_pullrequests_element.get_attribute('textContent') 
    except Exception as e:
        print(e)
        n_pullrequests_text=''

    try:
        n_contributors_element = browser.find_element(By.CSS_SELECTOR,n_contributors_selector)
        n_contributors_text = n_contributors_element.get_attribute('textContent')
    except Exception as e:
        print(e)
        n_contributors_text = '1'
    # except Exception as e:
    #     print('EXCEPTION BIG TRY #########################################################')
    #     # browser.savescre_enshot(f"{repo_url[19:].replace('/','_')}_1_screenshot.png")





    sleep(60)
    atribute_name = ['stars','watching','forks','commits','branches']
    atribute_dict={}
    text = watch_folk_text+n_commits_text+n_breanches_text
    try:
        for atribute   in  atribute_name:
            s=rf'(?P<n_{atribute}>\d+)\s*{atribute}'
            
            try:
                X = re.search(s, text)
                atribute_dict[atribute]= X.group(f'n_{atribute}')
            except Exception as e:
                print('no ', atribute)
                print(e)

        s = re.search(r'(?P<issues>\d+)',n_issues_text)
        p = re.search(r'(?P<Pullrequests>\d+)',n_pullrequests_text)
        c = re.search(r'(?P<contributors>\d+)',n_contributors_text)

        try:    
            atribute_dict['issues'] = s.group('issues')
        except Exception as e:
                print('no issues')
                print(e)

        try:    
            atribute_dict['pull requests'] = p.group('Pullrequests')
        except Exception as e:
                print('no Pullrequests')
                print(e)

        try:    
            atribute_dict['contributors'] = c.group('contributors')
        except Exception as e:
                print('no contributors')
                print(e)

    #     browser.close()
    #     print('Succsess. Browser closed')

    except Exception:
        print('error regex')
        # browser.save_screenshot(f"{repo_url[19:].replace('/','_')}_2_screenshot.png")
        sleep(15)
        browser.close()
        print('Failure. Browser closed')

    sleep(20)

    #return(watch_folk_text)
    return(atribute_dict)

if __name__ == 'main':
    github_vue_url= "https://github.com/aimeos/aimeos" 
    # github_vue_url= "https://github.com/BosNaufal/vue-mini-shop" 
    print(read_atributes(github_vue_url))