# modulo_pagination_slicing

* this new technique to handle pagention created correct for unlimited number fastest code speacfic for largest numbers of result can returned. ex latest number accepted by python as results and latest number acccepted if max group btns is 1 as page
  
* it not create any list bigger than 15 items and only loop 3 steps on this list as max
*  it uses math and modulo to calc the [prev, current which include page, next] groups with use of page number and (all calc as it done number+x operation same simple)
*  final use range after calc the very simple math operation and concat wiht modulo rule to get prev_start which first number in list and next_end (always max 2 numbers gap is 15) and all loop done with step on this max 15 or mx_btns*3 3 is referes to the 3 actions done in same loop dynamic prev, current, next

![image](https://github.com/MahmoudHegazi/modulo_pagination_slicing/assets/55125302/5e621da2-65bf-4246-89bc-166a882d845b)

# ex with max 5 buttons
![image](https://github.com/MahmoudHegazi/modulo_pagination_slicing/assets/55125302/7b95e99b-7854-47e8-a259-ab438686bbfa)
