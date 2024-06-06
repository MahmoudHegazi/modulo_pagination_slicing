import time
start = time.time() * 1000
total_btns = 1233444444444412111321131212121221212122121212121321443432342
page = 665656
mx_btns = 3
print("prossing {} items, target page is {} with max btns of each group set to: {}".format(total_btns, page, mx_btns))
# no loop even done to create it math 0 loop so this number not saw it
main_start = (page-(page%mx_btns)) if page%mx_btns != 0 else (page-(mx_btns))
prev_start = max((main_start-(mx_btns-1)), 1)
next_end = min((main_start + (mx_btns*2))+1, total_btns+1)
#print(prev_start)
#print(main_start)
#print(next_end)
total_btns_lists = list(range(prev_start, next_end))
len_total_lists = len(total_btns_lists)

total5_btns = []
#print(total_btns_lists)
pag = {'btns': None, 'is_next': False, 'is_previous': False}


for i in range(0, len_total_lists, mx_btns):

    list_start = (i-(i%mx_btns))
    list_end = list_start + (mx_btns)
    btns_group = total_btns_lists[list_start:list_end]
    
    if page in btns_group:
        pag['btns'] = [{'index': btn_i, 'current': True if page == btn_i else False} for btn_i in btns_group]
    else:
        if pag['btns'] is None and len(btns_group) > 0:
            pag['is_previous'] = btns_group[-1]
        elif pag['btns'] is not None and len(btns_group) > 0 and not pag['is_next']:
            pag['is_next'] = btns_group[0]
        else:
            break
end = time.time() * 1000
print("prossing time: {}".format((end-start)))
import json
print(json.dumps(pag,indent=4))

#for i in range(0, len(a), 5):
#    print(a[i:i+5])
