# --- Gerrit Coetzee 2018


import logging
import pickle
import os


class pickleking(object):
    def __init__(self, datadir="data"):
        self._datadir = datadir
        self._data = {}

    def load_data(self):
        f = open("./"+self._datadir+"/"+"data.pickle", "rb")
        data = pickle.load(f)
        f.close()
        logging.info("loading data successful")
        self._data = data
        return data

    def save_data(self, data):
        if not os.path.exists(self._datadir):
            os.mkdir(self._datadir)
            logging.info("Directory " + self._datadir + " Created ")
        else:
            logging.info("Directory " + self._datadir + " already exists")
        f = open("./"+self._datadir+"./"+"data.pickle", "wb")
        pickle.dump(self._data, f)
        f.close()


# PICKLECKING


#                                                                                          ,#@@%*%@#.
#                                                                                      #@(             .&(
#                                                                                   &@,                     &
#                                                                                /@*                           &
#                                                                              .@*                               %.
#                                                                             @/       @*#%#%#.%&*                #
#                                                                           *@         @/%@%%**     %/               .
#                                                                          @(                     %%   @              #
#                                                                         @*      #..               .&  */             (
#                                                                        @.    *(      (&             ,(  @            ,
#                                                                       @    .&           &            ,*  *            ,
#                                                                     .@     /     # #     #            ,%*/            @
#                                                                    ,@     .#     #       ,,%@/**%@#.                  %
#                                                                   /&       /             @           @                .
#                                                                  /@       @#*           @             &
#                                                                 %(        ,/ (#       &(.      (&      *              *
#                                                                @/   @#  .%& &(   ,,@   *,      #      .*              %
#                                                              .@   @  @@@@@%      &      #             @               #
#                                                             .@   & %@@@@@@.@/   @    &.  ,#         .&               ,
#                                                            %&    @ @@@@@@@@  %. @,@*     (  .@#%&                  @
#                                                           &(     & @@@@@@@@@@( @.         (#                        *,
#                                                          @.       @ @@@@@@@@@@&@ .@  @%@&,                          &
#                                                         @.         # %(@@@@@@@@@@@@&@@&@@@(@@  &,                  &
#                                                       .@   /        & &@,@@@@@@@@@@@@@@@@@@@@@@ **                *,
#                                                      .@ @@@#          @,&@@@@@@@@@@(@@#@@@@@@@@ @                &
#                                                     .@ .@@#               /@* (@@@@@@@@@@@@@@@@@ @               @
#                                                    /@                        %@  &@ @@@@@@@@@@@/ %              /.
#                                                   ##                             (@/...#&(@@@& &/              *#
#                                                  ##                                         *@,                #
#                                                 %/                                                            &
#                                                &/                                                            @
#                                               @                                                             @
#                                              @                                                             @
#                                             @                                                             &
#                                            @                                                             ,*
#                                          *#                                                              #
#                                         #*                                                             .@
#                                        @                                                              .%
#                                      .&                                                              .%
#                                     %*                                                               %
#                                    @                                                                @
#                                  #(  @@,                                                           &
#                                 @    @#                                                           @
#                               /(                                                      @%         %
#                              &                                                      /@@@        *
#                            (%                                                      ,&@@        %.
#                           @                                                                   %.
#                         &                                                                    @
#                       (*                                                                    @
#                     ,*                                                                     @
#                   .#                                                                     .&
#                  @                                                                      ,/
#                @,                                                                      @*
#              .&             *//                                                       @
#             %.             @@@@                                                      @
#           .#  .,.          #&                                                      *&
#          (, (@@@@                                                                 **
#         @   .@@@                                                                 &
#       **                                                                        @
#      #,                                                                       /%
#     #,                                                                       @,
#    @/                                                                      &&
#   //                                                                     ,@
#  .@                                                                    ,@
#  @                                                                    @,
# .%                                                ,@@#              %(
# &,                                               @@@@@            #&
# @                                               #@@@@*          *@
# @                                                             ,@
# @                                                           .@
# @                                                         .@
# @                                                       .@
# ,%                                                    *@
#  &,                                                 #&
#   %/                                              &(
#                                              &@
#       ,@(                                  #@&
#           /@@*                       .#@@*
#                ,#@@%/,       ,*%@@@*
