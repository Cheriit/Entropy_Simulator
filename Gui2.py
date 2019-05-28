# def generate_frames(self):
#     frame_start = Frame(master=self, background='#F3E77F')
#     frame_start.place(x=1, y=1, width=self.frames_numbers * 51, height=78)
#
#     for i in range(1, self.frames_numbers + 1):
#         for j in range(1, (self.frames_numbers // 2) + 1):
#             if i == 1:
#                 fr = Frame(master=self,
#                            background='#D5E88F')
#             else:
#                 fr = Frame(master=self,
#                            background='#889E9D')
#
#             fr.place(x=(i + 50 * (i - 1)), y=105 + j + 50 * (j - 1), width=50, height=50)
#
#     return frame_start
