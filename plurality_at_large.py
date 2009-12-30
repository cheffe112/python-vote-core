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

from voting_system import VotingSystem
import copy, types

# This class implements plurality at large (aka block voting).
class PluralityAtLarge(VotingSystem):
    
    @staticmethod
    def calculate_winner(ballots, required_winners = 1):
        result = {}
        
        # Parse the incoming candidate list
        candidates = set()
        for ballot in ballots:
            
            # Convert single candidate ballots into ballot lists
            if type(ballot["ballot"]) != types.ListType:
                ballot["ballot"] = [ballot["ballot"]]
                
            # Ensure no ballot has an excess of candidates
            if len(ballot["ballot"]) > required_winners:
                raise Exception("A ballot contained too many candidates")
            
            # Observe all mentioned candidates 
            for candidate in ballot["ballot"]:
                candidates.add(candidate)
        
        # Ensure we have sufficient candidates
        if len(candidates) < required_winners:
            raise Exception("Insufficient candidates to meet produce sufficient winners")
        
        # Generate tie breaker, which may or may not be used later
        tie_breaker = PluralityAtLarge.generate_tie_breaker(candidates)

        # Sum up all votes for each candidate
        tallies = dict.fromkeys(candidates, 0)
        for ballot in ballots:
            for candidate in ballot["ballot"]:
                tallies[candidate] += ballot["count"]
        result["tallies"] = copy.deepcopy(tallies)
        
        # Determine which candidates win
        winning_candidates = set()
        while len(winning_candidates) < required_winners:
            
            # Find the remaining candidates with the most votes
            largest_tally = max(tallies.values())
            top_candidates = PluralityAtLarge.matching_keys(tallies, largest_tally)
            
            # Reduce the found candidates if there are too many
            if len(top_candidates | winning_candidates) > required_winners:
                result["tie_breaker"] = tie_breaker
                result["tied_winners"] = top_candidates.copy()
                while len(top_candidates | winning_candidates) > required_winners:
                    top_candidates.remove(PluralityAtLarge.break_ties(top_candidates, tie_breaker, True))
            
            # Move the top candidates into the winning pile
            winning_candidates |= top_candidates
            for candidate in top_candidates:
                del tallies[candidate]
                
        # Return the final result
        result["winners"] = winning_candidates
        return result