

class OTOParameters:
    offset: float
    overlap: float
    preutterance: float
    fixed: float
    cutoff: float

class OTOLine:
    alias: str
    wav_file_name: str
    timing_data: OTOParameters

class OTOFile:
    oto_line_list: list[OTOLine]

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
                oto_line.alias = OTOAlias(alias=alias_part)
                oto_line.wav_file_name = wav_file_name
                oto_line.timing_data = OTOParameters(offset=float(offset), overlap=float(overlap), preutterance=float(preutterance), fixed=float(fixed), cutoff=float(cutoff))
                self.oto_line_list.append(oto_line)

    def write_oto_file(self, file_path: str):
        with open(file_path, 'w', encoding='utf-8') as f:
            for oto_line in self.oto_line_list:
                line = f"{oto_line.alias}={oto_line.wav_file_name},{oto_line.timing_data.offset},{oto_line.timing_data.overlap},{oto_line.timing_data.preutterance},{oto_line.timing_data.fixed},{oto_line.timing_data.cutoff}\n"
                f.write(line)

