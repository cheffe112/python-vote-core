from pyvotecore.condorcet import CondorcetHelper
from pyvotecore.schulze_npr import SchulzeNPR

ballots_test = [ { "count":4, "ballot":[["a"], ["b"], ["c"], ["d"]] }, { "count":4, "ballot":[["a"], ["c"], ["b"], ["d"]] }, { "count":4, "ballot":[["a"], ["d"], ["b"], ["c"]] }, { "count":4, "ballot":[["a"], ["b"], ["d"], ["c"]] }, { "count":4, "ballot":[["a"], ["b"], ["c"], ["d"]] } ]
ballots_scene1 = [ { "count":12, "ballot":[["d"], ["c"], ["a"], ["b"]] }, { "count":7, "ballot":[["c"], ["d"], ["a"], ["b"]] }, { "count":6, "ballot":[["d"], ["a"], ["c"], ["b"]] }, { "count":1, "ballot":[["c"], ["d"], ["b"], ["a"]] } ]
ballots_scene2 = [ { "count":11, "ballot":[["b"], ["d"], ["c"], ["a"]] }, { "count":6, "ballot":[["b"], ["a"], ["c"], ["d"]] }, { "count":5, "ballot":[["b"], ["a"], ["d"], ["c"]] }, { "count":1, "ballot":[["a"], ["b"], ["d"], ["c"]] }, { "count":1, "ballot":[["b"], ["c"], ["a"], ["d"]] }, { "count":1, "ballot":[["c"], ["b"], ["a"], ["d"]] } ]
ballots_scene3 = [ { "count":8, "ballot":[["b"], ["a"], ["c"], ["d"]] }, { "count":7, "ballot":[["b"], ["a"], ["d"], ["c"]] }, { "count":4, "ballot":[["b"], ["d"], ["a"], ["c"]] }, { "count":3, "ballot":[["d"], ["b"], ["a"], ["c"]] }, { "count":1, "ballot":[["b"], ["c"], ["a"], ["d"]] }, { "count":1, "ballot":[["c"], ["a"], ["d"], ["b"]] }, { "count":1, "ballot":[["d"], ["c"], ["b"], ["a"]] } ]
ballots_scene4 = [ { "count":12, "ballot":[["c"], ["a"], ["b"], ["d"]] }, { "count":6, "ballot":[["c"], ["b"], ["a"], ["d"]] }, { "count":1, "ballot":[["a"], ["c"], ["d"], ["b"]] }, { "count":1, "ballot":[["b"], ["a"], ["c"], ["d"]] }, { "count":1, "ballot":[["b"], ["c"], ["a"], ["d"]] }, { "count":1, "ballot":[["c"], ["a"], ["d"], ["b"]] }, { "count":1, "ballot":[["d"], ["a"], ["b"], ["c"]] }, { "count":1, "ballot":[["d"], ["b"], ["a"], ["c"]] }, { "count":1, "ballot":[["d"], ["b"], ["c"], ["a"]] } ]

voting = SchulzeNPR(ballots_scene4, ballot_notation = CondorcetHelper.BALLOT_NOTATION_GROUPING).as_dict()
final_ranking = []
for winner in voting['rounds']:
    final_ranking.append(winner['winner'])
print final_ranking
print voting['preferences']

