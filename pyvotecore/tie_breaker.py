# Copyright (C) 2009, Brad Beattie
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from copy import copy
import random
import types


# This class provides tie breaking methods
class TieBreaker(object):

    #
    def __init__(self, candidate_range):
        self.ties_broken = False
        self.candidates = list(candidate_range)
        if not isinstance(candidate_range, types.ListType):
            random.shuffle(self.candidates)

    #
    def break_ties(self, tied_candidates, reverse=False):
        self.ties_broken = True
        candidates = copy(self.candidates)
        if reverse:
            candidates.reverse()
        if getattr(list(tied_candidates)[0], '__iter__', False):
            result = self.break_complex_ties(tied_candidates, candidates)
        else:
            result = self.break_simple_ties(tied_candidates, candidates)
        return result

    #
    @staticmethod
    def break_simple_ties(tied_candidates, candidates):
        for candidate in candidates:
            if candidate in tied_candidates:
                return candidate

    #
    @staticmethod
    def break_complex_ties(tied_candidates, candidates):
        max_columns = len(list(tied_candidates)[0])
        column = 0
        while len(tied_candidates) > 1 and column < max_columns:
            min_index = min(candidates.index(list(candidate)[column]) for candidate in tied_candidates)
            tied_candidates = set([candidate for candidate in tied_candidates if candidate[column] == candidates[min_index]])
            column += 1
        return list(tied_candidates)[0]

    #
    def as_list(self):
        return self.candidates

    #
    def __str__(self):
        return "[%s]" % ">".join(self.candidates)
    
class ConsistentOrderTieBreaker(TieBreaker):
    
    def __init__(self, candidate_range):
        self.ties_broken = False
        self.candidates = list(candidate_range)

    def break_ties(self, tied_candidates, reverse=False):
        self.ties_broken = True
        candidates = copy(self.candidates)
        if reverse:
            candidates.reverse()
        
        for candidate in candidates:
            # TODO hash
            # TODO use tied candidates
            return candidate
