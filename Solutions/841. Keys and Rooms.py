#https://leetcode.com/problems/keys-and-rooms/submissions/862399791/

def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    rooms_to_visit = [0]
    found_keys = {0}

    while rooms_to_visit:
        cur_room = rooms_to_visit.pop()

        for key in rooms[cur_room]:
            if key in found_keys:
                continue
            else:
                found_keys.add(key)
                rooms_to_visit.append(key)

    return len(found_keys) == len(rooms)