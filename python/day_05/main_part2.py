import re

def convert_to_int(code):
    code = re.sub("[FL]", "0", code)
    code = re.sub("[BR]", "1", code)
    return int(code, 2)


if __name__ == "__main__":
    with open("day_05/input") as fp:
        seat_codes = fp.read().split()

    candidate_seat_ids = range(127*8+7+1)
    occupied_seat_ids = [convert_to_int(seat_code) for seat_code in seat_codes]

    # seat can not be occupied
    candidate_seat_ids = filter(lambda seat_id: seat_id not in occupied_seat_ids, candidate_seat_ids)

    # seat is not in first row
    candidate_seat_ids = filter(lambda seat_id: seat_id > 7, candidate_seat_ids)
    
    # seat is not in last row
    candidate_seat_ids = filter(lambda seat_id: seat_id <= 1023-8, candidate_seat_ids)
    
    # neighbour seats are occupied
    candidate_seat_ids = filter(lambda seat_id: seat_id +1 in occupied_seat_ids and seat_id -1 in occupied_seat_ids, candidate_seat_ids)
    
    candidate_seat_ids = list(candidate_seat_ids)
    
    print(f"Options left: {len(candidate_seat_ids)}")
    print(f"Options are: {candidate_seat_ids}")
