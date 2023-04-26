# You have 100 cats.
#
# One day you decide to arrange all your cats in a giant circle.
# Initially, none of your cats have any hats on. You walk around the circle
# 100 times, always starting at the same spot, with the first cat (cat # 1).
# Every time you stop at a cat, you either put a hat on it if it does not have
# # one on, or you take its hat off if it has one on.
#
# The first round, you stop at every cat, placing a hat on each one.
# The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you have made 100 rounds around the cats (e.g. you
# only visit the 100th cat). Write a program that simply outputs which cats have hats
# at the end.
# Optional: Make function that can calculate hat with any amount of rounds and cats.
#
# Here you should write an algorithm, after that, try to make pseudo code. Only after
# that start to work. Code is simple here, but you might struggle with algorithm.
#     Therefore don`t try to write a code from the first attempt.
def put_hats_cats(number_cats):
    # -1 means cat doesn't have hat
    cats = [-1] * number_cats
    hat_changes = 0
    go_every = 1
    while go_every < number_cats:
        for i in range(0+go_every-1, len(cats), go_every):
            cats[i] *= -1
            hat_changes += 1
        go_every += 1
    cat_hats = [j for j, x in enumerate(cats) if x > 0]
    return cat_hats, hat_changes

number_cats = 100
print(put_hats_cats(number_cats))
