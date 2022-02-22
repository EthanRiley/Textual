import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# List of Artists 
# INPUT DF, VARIABLE X , VARIABLE Y
artists_list = ["Drake_text", "Kanye_text", "Kendrick_text"]

#bins = np.linspace(70,140,20)

# --> df : first row is indexs/titles, second row is data
# --> get index of subj and pol from row 1, then get items from row 2 using that index
# --> then give it to the graph

def vis_2(dict, var_x, var_y):

    column_list = ['wordcount', 'numwords', 'raw', 'word length', 'polarity', 
    'subjectivity', 'vocab size', 'sentence length']

    x_idx = dict[var_x] # --> Dicts containng data
    y_idx = dict[var_y]

    x_data = df.iloc[x_idx] # --> dict
    y_data = df.iloc[y_idx] # --> dict
    artists = x_data.keys()
    x_data_val = x_data.values()


    '''
    
    x = series of x_var
    y = series of y_var

    plt.sub
    
    
    
    '''




    for idx, artist in enumerate(artists):
        plt.subplot(3, 1, idx + 1)
    
        # Boolean index to get the artist text and info
        one_artist = df['Text'] == artist
        one_artist_list = df.loc[one_artist, :]
    
        # Plotting the box plot
        sns.boxplot(x=x_data_val, y=one_artist_list[var_y], data=df) 
        
        plt.gca().title.set_text(artist)
    
        # adds space between each plot
        plt.subplots_adjust(hspace=1.5)

        # sets the size of each plot
        plt.gcf().set_size_inches((10, 5))

        # sets a limit on the y-axis
        plt.ylim(0, .05)

        # labels all x-axis
        plt.xlabel(var_x)
        plt.ylabel(var_y)
    
    
