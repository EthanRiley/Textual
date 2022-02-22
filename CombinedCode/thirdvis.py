from Textual import textual
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    tt = textual()
    songs = ['CombinedCode/Drake/cant_take_a_joke.txt', 'CombinedCode/Drake/dont_matter_to_me.txt', 
                'CombinedCode/Drake/nine.txt', 'CombinedCode/Drake/nonstop.txt', 
                'CombinedCode/Drake/redemption.txt', 'CombinedCode/Drake/views.txt', 
                'CombinedCode/Kanye/all_falls_down.txt', 'CombinedCode/Kanye/jesus_walks.txt', 
                'CombinedCode/Kanye/dark_fantasy.txt', 'CombinedCode/Kanye/never_let_me_down.txt', 
                'CombinedCode/Kanye/power.txt', 'CombinedCode/Kanye/runaway.txt', 
                'CombinedCode/Kendrick/alright.txt', 'CombinedCode/Kendrick/blacker_the_berry.txt', 
                'CombinedCode/Kendrick/dont_kill_my_vibe.txt', 'CombinedCode/Kendrick/king_kunta.txt', 
                'CombinedCode/Kendrick/maad_city.txt', 'CombinedCode/Kendrick/money_trees.txt']
    song_names = ['cant_take_a_joke', 'dont_matter_to_me', 'nine', 'nonstop', 'redemption', 'views',
                'all_falls_down', 'jesus_walks', 'dark_fantasy', 'never_let_me_down', 'power', 'runaway',
                'alright', 'blacker_the_berry', 'dont_kill_my_vibe', 'king_kunta', 'maad_city', 'money_trees']

    for i in range(len(songs)):
        tt.load_text(songs[i], song_names[i], parser=textual.txt_parser)

    songs_list = tt.data['polarity'].keys()
    avg_word_length = tt.data['word length'].values()
    vocab_size = tt.data['vocab size'].values()
    songs_df = pd.DataFrame()
    songs_df['Artists'] = ['Drake', 'Drake', 'Drake', 'Drake', 'Drake', 'Drake', 
            'Kanye', 'Kanye', 'Kanye', 'Kanye', 'Kanye', 'Kanye', 
            'Kendrick', 'Kendrick', 'Kendrick', 'Kendrick', 'Kendrick', 'Kendrick',]
    songs_df['song_name'] = songs_list
    songs_df['word_length'] = avg_word_length
    songs_df['vocab_size'] = vocab_size
    sns.set()
    sns.scatterplot(data=songs_df, x='word_length', y='vocab_size', hue='Artists')
    plt.savefig('vocab_vs_word.png')

main()



