# coding: utf-8

def main(rand_str,find_str):

    rand_length = len(rand_str)
    match = 0
    for f in find_str:
        match = rand_str.find(f,match,rand_length)
        print match
#    print nepolitan

if __name__ == "__main__":
    spagetti = """-------
gtgtsgipgttptinggipsppaigsesgpetgstpatetisiesagaeaigttetepitiatsegssieeeeatepaaiagtpieataatppiitgiapsteitatiiatpetetetttgpetpaasipttssstpeeeggtiagtttegtiipestsasgpsepaasapttgattgiatppegitiatpasgatgepttggapesaeetaeissttggieietgspagesiipestipggstttpateptitiaetottissgggtttaipappgstsptttgtpispattgegstltiappseisapgistaiagteeiptptpisaieisagstapeteietgteiisgtiptstgtstasspeatspptitttatteastsgtptgtasggpniaaeteaisett
-------"""

    find_str = "neapolitan"

    main(spagetti,find_str)
