import utau_dev_tools

def make_vcv(initial, medial, final):
    return f"{initial} {medial}{final}"

utau_dev_tools.convert_reclist_to_comment("test_data/test_reclist/test_reclist.txt", "test_data/test_reclist/test_output_reclist.txt", "test_data/test_reclist/test_comment.txt")