import pandas as pd
import Player
import pickle


year_to_study = 2018

df_players = pd.read_csv('Data/atp_players.csv', header=None, names=[1, 2, 3, 4, 5, 6], encoding="ISO-8859-1")
df_matches_year_to_study = pd.read_csv('Data/atp_matches_%i.csv' % year_to_study)
df_matches_year_to_study = df_matches_year_to_study.sort_values(by='tourney_date').reset_index()
print(df_matches_year_to_study)

list_players_year_to_study = {}
for row in range(len(df_matches_year_to_study)):
    id_winner = df_matches_year_to_study['winner_id'][row]
    id_loser = df_matches_year_to_study['loser_id'][row]
    height_winner = df_matches_year_to_study['winner_ht'][row]
    hand_winner = df_matches_year_to_study['winner_hand'][row]
    height_loser = df_matches_year_to_study['loser_ht'][row]
    hand_loser = df_matches_year_to_study['loser_hand'][row]
    list_players_year_to_study[id_winner] = [height_winner, hand_winner]
    list_players_year_to_study[id_loser] = [height_loser, hand_loser]

players_list = []
players_list_dict = {}

for row in range(len(df_players)):
    id_nb = df_players[1][row]
    if id_nb in list_players_year_to_study.keys():
        name = str(df_players[2][row]) + ' ' + str(df_players[3][row])
        born_year = str(df_players[5][row])[:4]
        country = str(df_players[6][row])
        player = Player.Player(name, born_year, country, id_nb)
        hand = list_players_year_to_study[id_nb][1]
        height = list_players_year_to_study[id_nb][0]
        if hand != 'nan'and hand == hand:
            player.hand = list_players_year_to_study[id_nb][1]
        if height != 'nan' and height == height:
            player.height = list_players_year_to_study[id_nb][0]
        players_list.append(player)
        players_list_dict[player.id] = player

for year in range(1980, year_to_study):
    df_matches_year = pd.read_csv('Data/atp_matches_%i.csv' % year)
    for row in range(len(df_matches_year)):
        id_winner = df_matches_year['winner_id'][row]
        id_loser = df_matches_year['loser_id'][row]
        tournament_date = str(df_matches_year['tourney_date'][row])
        score = df_matches_year['score'][row]
        if score == score and type(score) == str:
            sets_number = score.count('-')
        else:
            sets_number = -1
        surface = df_matches_year['surface'][row]

        w_ace = df_matches_year['w_ace'][row]
        w_svpt = df_matches_year['w_svpt'][row]
        w_df = df_matches_year['w_df'][row]
        w_1stwon = df_matches_year['w_1stWon'][row]
        w_2ndwon = df_matches_year['w_2ndWon'][row]
        w_1stIn = df_matches_year['w_1stIn'][row]
        w_bp_Saved = df_matches_year['w_bpSaved'][row]
        w_bp_Faced = df_matches_year['w_bpFaced'][row]
        w_SvGms = df_matches_year['w_SvGms'][row]

        l_ace = df_matches_year['l_ace'][row]
        l_svpt = df_matches_year['l_svpt'][row]
        l_df = df_matches_year['l_df'][row]
        l_1stwon = df_matches_year['l_1stWon'][row]
        l_2ndwon = df_matches_year['l_2ndWon'][row]
        l_1stIn = df_matches_year['l_1stIn'][row]
        l_bp_Saved = df_matches_year['l_bpSaved'][row]
        l_bp_Faced = df_matches_year['l_bpFaced'][row]
        l_SvGms = df_matches_year['l_SvGms'][row]

        # print('sets number', sets_number)
        # for player in players_list:
        #     if player.id == id_winner:
        #         player.add_victory(id_loser)
        #         player.last_tournament_date = tournament_date
        #         player.update_fatigue(tournament_date, sets_number)
        #         player.update_surface_victory_percentage(surface, 'V')
        #         if w_svpt == w_svpt and w_ace == w_ace:
        #             player.update_ace_percentage(w_ace, w_svpt)
        #         if w_svpt == 0:
        #             print('div by 0', row)
        #         if w_svpt == w_svpt and w_df == w_df:
        #             player.update_doublefault_percentage(w_df, w_svpt)
        #         if w_svpt == w_svpt and w_1stwon == w_1stwon and w_2ndwon == w_2ndwon:
        #             player.update_winning_on_1st_serve_percentage(w_1stwon, w_svpt)
        #             player.update_winning_on_2nd_serve_percentage(w_2ndwon, w_svpt)
        #         if w_svpt == w_svpt and w_1stIn == w_1stIn:
        #             player.update_first_serve_success_percentage(w_1stIn, w_svpt)
        #         if w_bp_Faced == w_bp_Faced and w_bp_Saved == w_bp_Saved and w_SvGms == w_SvGms:
        #             player.update_breakpoint_faced_and_savec(w_bp_Faced, w_bp_Saved, w_SvGms)
        #
        #     elif player.id == id_loser:
        #         player.add_defeat(id_winner)
        #         player.last_tournament_date = tournament_date
        #         player.update_fatigue(tournament_date, sets_number)
        #         player.update_surface_victory_percentage(surface, 'D')
        #         if l_svpt == l_svpt and l_ace == l_ace:
        #             player.update_ace_percentage(l_ace, l_svpt)
        #         if l_svpt == l_svpt and l_df == l_df:
        #             player.update_doublefault_percentage(l_df, l_svpt)
        #         if l_svpt == l_svpt and l_1stwon == l_1stwon and l_2ndwon == l_2ndwon:
        #             player.update_winning_on_1st_serve_percentage(l_1stwon, l_svpt)
        #             player.update_winning_on_2nd_serve_percentage(l_2ndwon, l_svpt)
        #         if l_svpt == l_svpt and l_1stIn == l_1stIn:
        #             player.update_first_serve_success_percentage(l_1stIn, l_svpt)
        #         if l_bp_Faced == l_bp_Faced and l_bp_Saved == l_bp_Saved and l_SvGms == l_SvGms:
        #             player.update_breakpoint_faced_and_savec(l_bp_Faced, l_bp_Saved, l_SvGms)

        try:
            winner = players_list_dict[id_winner]

            winner.add_victory(id_loser)
            winner.last_tournament_date = tournament_date
            winner.update_fatigue(tournament_date, sets_number)
            winner.update_surface_victory_percentage(surface, 'V')
            if w_svpt == w_svpt and w_ace == w_ace:
                winner.update_ace_percentage(w_ace, w_svpt)
            if w_svpt == 0:
                print('div by 0', row)
            if w_svpt == w_svpt and w_df == w_df:
                winner.update_doublefault_percentage(w_df, w_svpt)
            if w_svpt == w_svpt and w_1stwon == w_1stwon and w_2ndwon == w_2ndwon:
                winner.update_winning_on_1st_serve_percentage(w_1stwon, w_svpt)
                winner.update_winning_on_2nd_serve_percentage(w_2ndwon, w_svpt)
            if w_svpt == w_svpt and w_1stIn == w_1stIn:
                winner.update_first_serve_success_percentage(w_1stIn, w_svpt)
            if w_bp_Faced == w_bp_Faced and w_bp_Saved == w_bp_Saved and w_SvGms == w_SvGms:
                winner.update_breakpoint_faced_and_savec(w_bp_Faced, w_bp_Saved, w_SvGms)
        except:
            # print("Winner no longer playing in %i" % year_to_study)
            pass

        try:
            loser = players_list_dict[id_loser]

            loser.add_defeat(id_winner)
            loser.last_tournament_date = tournament_date
            loser.update_fatigue(tournament_date, sets_number)
            loser.update_surface_victory_percentage(surface, 'D')
            if l_svpt == l_svpt and l_ace == l_ace:
                loser.update_ace_percentage(l_ace, l_svpt)
            if l_svpt == l_svpt and l_df == l_df:
                loser.update_doublefault_percentage(l_df, l_svpt)
            if l_svpt == l_svpt and l_1stwon == l_1stwon and l_2ndwon == l_2ndwon:
                loser.update_winning_on_1st_serve_percentage(l_1stwon, l_svpt)
                loser.update_winning_on_2nd_serve_percentage(l_2ndwon, l_svpt)
            if l_svpt == l_svpt and l_1stIn == l_1stIn:
                loser.update_first_serve_success_percentage(l_1stIn, l_svpt)
            if l_bp_Faced == l_bp_Faced and l_bp_Saved == l_bp_Saved and l_SvGms == l_SvGms:
                loser.update_breakpoint_faced_and_savec(l_bp_Faced, l_bp_Saved, l_SvGms)
        except:
            # print('Loser no longer playing in %i' % year_to_study)
            pass

for player in players_list_dict.values():
    print(player)
    print('          Last Matches :  ', player.last_matches, ' *** Victory Percentage : ', player.victory_percentage,
          '%')
    print('           *** Ace Percentage : ', player.ace_percentage, '%')
    print('           *** Double Fault Percentage : ', player.doublefault_percentage, '%')
    print('           *** Serve Point Won Percentage : ', player.overall_win_on_serve_percentage, '%')
    print('           *** Serve Point In Percentage : ', player.first_serve_success_percentage, '%')
    print('           *** BreakPoint Faced : ', player.breakpoint_faced_percentage, '%', '   *** Breakpoint Saved : ',
          player.breakpoint_saved_percentage, '%')
    if player.id == 104745 or player.id == 104932:
        print(player.matches)

'''
with open('Players_%i_profiles' % year_to_study, 'wb') as file:
    my_pickler = pickle.Pickler(file)
    my_pickler.dump(players_list_dict)
'''

df_data_players = pd.DataFrame(columns=['name', 'id',  'ranking', 'ranking_points', 'born_year', 'versus', 'hand',
                                        'height',
                                        'victory_percentage', 'clay_victory_percentage', 'carpet_victory_percentage',
                                        'grass_victory_percentage', 'hard_victory_percentage', 'ace_percentage',
                                        'doublefault_percentage', 'first_serve_success_percentage',
                                        'winning_on_1st_serve_percentage', 'winning_on_2nd_serve_percentage',
                                        'overall_win_on_serve_percentage', 'breakpoint_faced_percentage',
                                        'breakpoint_saved_percentage'])
print(df_data_players)
for player in players_list_dict.keys():
    df_to_add = pd.DataFrame([players_list_dict[player].get_data_profile()],
                                            columns=['name', 'id',  'ranking', 'ranking_points', 'born_year', 'versus',
                                                     'hand', 'height', 'victory_percentage', 'clay_victory_percentage',
                                                     'carpet_victory_percentage', 'grass_victory_percentage',
                                                     'hard_victory_percentage', 'ace_percentage',
                                                     'doublefault_percentage', 'first_serve_success_percentage',
                                                     'winning_on_1st_serve_percentage',
                                                     'winning_on_2nd_serve_percentage',
                                                     'overall_win_on_serve_percentage',
                                                     'breakpoint_faced_percentage',  'breakpoint_saved_percentage'])

    df_data_players = df_data_players.append(df_to_add)

df_data_players.to_csv('Players_Statistics_.csv', index=False)
