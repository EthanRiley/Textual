from Textual import textual
import pandas as pd

def main():
    tt = textual()

    drake_views_songs = ['CombinedCode/Drake/nine.txt', 'CombinedCode/Drake/redemption.txt', 'CombinedCode/Drake/views.txt']
    drake_scorpion_songs = ['CombinedCode/Drake/cant_take_a_joke.txt', 'CombinedCode/Drake/dont_matter_to_me.txt', 'CombinedCode/Drake/nonstop.txt']

    drake_views = textual.combine_txt(drake_views_songs)
    drake_scorpion = textual.combine_txt(drake_scorpion_songs)
    
    kanye_mbdtf_songs= ['CombinedCode/Kanye/dark_fantasy.txt','CombinedCode/Kanye/power.txt', 'CombinedCode/Kanye/runaway.txt']
    kanye_tcdo_songs = ['CombinedCode/Kanye/all_falls_down.txt', 'CombinedCode/Kanye/jesus_walks.txt', 'CombinedCode/Kanye/never_let_me_down.txt', ]

    kanye_mbdtf = textual.combine_txt(kanye_mbdtf_songs)
    kanye_tcdo = textual.combine_txt(kanye_tcdo_songs) 

    kendrick_maad_songs = ['CombinedCode/Kendrick/dont_kill_my_vibe.txt', 'CombinedCode/Kendrick/maad_city.txt', 'CombinedCode/Kendrick/money_trees.txt']
    kendrick_tpab_songs = ['CombinedCode/Kendrick/alright.txt', 'CombinedCode/Kendrick/blacker_the_berry.txt', 'CombinedCode/Kendrick/king_kunta.txt', ]

    kendrick_maad= textual.combine_txt(kendrick_maad_songs)
    kendrick_tpab = textual.combine_txt(kendrick_tpab_songs) 

    tt.load_text(drake_views, 'Views')
    tt.load_text(drake_scorpion, 'Scorpion')
    tt.load_text(kanye_mbdtf, 'MBDTF')
    tt.load_text(kanye_tcdo, 'TCDO')
    tt.load_text(kendrick_maad, 'MAAD')
    tt.load_text(kendrick_tpab, 'TPAB')

    songs_list = tt.data['polarity'].keys()
    polarity = tt.data['polarity'].values()
    subjectivity = tt.data['subjectivity'].values()

    songs_df = pd.DataFrame()
    songs_df['Artists'] = ['Drake', 'Drake', 'Kanye', 'Kanye', 'Kendrick', 'Kendrick']
    songs_df['Album_name'] = songs_list
    songs_df['Polarity'] = polarity
    songs_df['Subjectivity'] = subjectivity

    print(polarity)
    print(songs_list)
    print(subjectivity)


    #songs_a = songs_df[songs_df['Song_name'] == 'Kanye']
    # print(songs_df.loc[songs_df['Artists'] == 'Drake'])

    #tt.make_boxplots(songs_df, 'Artists', 'Polarity')

 #   print(songs_df)

main()
    
