
# ReclistHelpers is for making the reclist itself
# OTOHelpers is for making the oto file itself as well as modifying them

class Reclist:
    reclist_lines = list[str]
    comment_lines = list[tuple[int, str]]

def convert_reclist_to_comment(base_reclist_path: str, final_reclist_path: str, comment_output_path: str):
    reclist_file_lines = []
    comment_lines = []
    with open(base_reclist_path, 'r', encoding='utf-8') as f:
        reclist_lines = f.readlines()
        for i, line in enumerate(reclist_lines):
            line = line.strip()
            if not line:
                continue
            comment_lines.append(f'{str(i).zfill(5)}\t{line}\n')
            reclist_file_lines.append(f'{str(i).zfill(5)}\n')
    with open(comment_output_path, 'w', encoding='utf-8') as f:
        f.writelines(comment_lines)
    with open(final_reclist_path, 'w', encoding='utf-8') as f:
        f.writelines(reclist_file_lines)




class OTOParameters:
    offset = float
    overlap = float
    preutterance = float
    fixed = float
    cutoff = float

class OTOLine:
    alias = str
    wav_file_name = str
    timing_data = OTOParameters

class OTOFile:
    oto_line_list = list[OTOLine]

    def add_phoneme(self, alias:str, wav_file_name:str, parameters:OTOParameters):
        oto_line = OTOLine()
        oto_line.alias = alias
        oto_line.wav_file_name = wav_file_name
        oto_line.timing_data = parameters
        self.oto_line_list.append(oto_line)

    def remove_phoneme(self, alias:str):
        self.oto_line_list = [line for line in self.oto_line_list if line.alias != alias]

    def read_oto_file(self, file_path: str):
        self.oto_line_list = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                alias_part, data_part = line.split('=')
                wav_file_name, offset, fixed, cutoff, preutterance, overlap = data_part.split(',')
                oto_line = OTOLine()
                oto_line.alias = alias_part
                oto_line.wav_file_name = wav_file_name
                oto_line.timing_data = OTOParameters(offset=float(offset), overlap=float(overlap), preutterance=float(preutterance), fixed=float(fixed), cutoff=float(cutoff))
                self.oto_line_list.append(oto_line)

    def write_oto_file(self, file_path: str):
        with open(file_path, 'w', encoding='utf-8') as f:
            for oto_line in self.oto_line_list:
                line = f"{oto_line.alias}={oto_line.wav_file_name},{oto_line.timing_data.offset},{oto_line.timing_data.overlap},{oto_line.timing_data.preutterance},{oto_line.timing_data.fixed},{oto_line.timing_data.cutoff}\n"
                f.write(line)

    def modify_phoneme(self, OTOFile,  alias:str, new_parameters:OTOParameters):
        for oto_line in self.oto_line_list:
            if oto_line.alias == alias:
                oto_line.timing_data = new_parameters
                break
            else:
                print(f"Phoneme with alias '{alias}' not found in OTO file.")