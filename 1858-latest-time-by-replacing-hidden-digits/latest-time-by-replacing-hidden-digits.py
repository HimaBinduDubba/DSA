class Solution:
    def maximumTime(self, time: str) -> str:
       time = list(time)  # Convert string to list to allow modification

        # Hour - First digit
       if time[0] == '?':
            if time[1] == '?' or time[1] <= '3':
                time[0] = '2'
            else:
                time[0] = '1'

        # Hour - Second digit
       if time[1] == '?':
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'

        # Minute - First digit
       if time[3] == '?':
            time[3] = '5'

        # Minute - Second digit
       if time[4] == '?':
            time[4] = '9'

       return ''.join(time)