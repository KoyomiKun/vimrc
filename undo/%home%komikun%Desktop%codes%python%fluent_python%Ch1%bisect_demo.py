Vim�UnDo� �z����$�-Y[(3��͛Bd��g�X�Z���      3    index = bisect.bisect_left(break_points, score)            /       /   /   /    _�    _�                            ����                                                                                                                                                                                                                                                                                                                                                             _��     �               "        offset = position * '   |'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _��     �               !        offset = position * '  |'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _��     �                        offset = position * ' |'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _��    �                       offset = position * '|'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _�	    �               !        offset = position * '  |'5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             _��    �      
         #fmt = '{0:2d} @ {1:2d}  {2}{0:<2d}'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             _��     �               #        offset = position * '    |'5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             _��   
 �               "        offset = position * '   |'5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             _��    �               !        offset = position * '  |'5�_�   	              
   	       ����                                                                                                                                                                                                                                                                                                                                                             _��    �      
         %fmt = '{0:2d} @ {1:2d}    {2}{0:<2d}'5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                  V        _�     �                *haystack = [1, 3, 5, 7, 9, 11, 13, 17, 19]   needles = [2, 4, 6, 8, 10]       'fmt = '{0:2d} @ {1:2d}      {2}{0:<2d}'           def demo(bisect_fn):   $    for needle in reversed(needles):   .        position = bisect_fn(haystack, needle)            offset = position * ' |'   3        print(fmt.format(needle, position, offset))           if sys.argv[-1] == "left":   "    bisect_fn = bisect.bisect_left   else:       bisect_fn = bisect.bisect       "print("demo:", bisect_fn.__name__)   :print('haystack ->', ''.join('%2d' % n for n in haystack))   demo(bisect_fn)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        _�     �                 
import sys    �                  5�_�                          ����                                                                                                                                                                                                                                                                                                                               
          
       V        _
     �                 def5�_�                           ����                                                                                                                                                                                                                                                                                                                               
          
       V        _     �                 def5�_�                       1    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _0     �                 2def grading(score, break_points=[0, 60, 80, 90, ])5�_�                       1    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _6     �                 2def grading(score, break_points=[0, 60, 80, 90, ] 5�_�                       1    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _9     �                 3def grading(score, break_points=[0, 60, 80, 90, ]) 5�_�                       =    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _S     �                 @def grading(score, break_points=[0, 60, 80, 90, ], grades='FC') 5�_�                      A    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _]     �                 Bdef grading(score, break_points=[0, 60, 80, 90, ], grades='FCBA') 5�_�                            ����                                                                                                                                                                                                                                                                                                                               
          
       V        _j     �                  5�_�                       "    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �               Bdef grading(score, break_points=[0, 60, 80, 90, ], grades='FCBA'):5�_�                       "    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �               Adef grading(score, break_points=[0 60, 80, 90, ], grades='FCBA'):5�_�                            ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �               @def grading(score, break_points=[060, 80, 90, ], grades='FCBA'):5�_�                            ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �               ?def grading(score, break_points=060, 80, 90, ], grades='FCBA'):5�_�                            ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �               >def grading(score, break_points=60, 80, 90, ], grades='FCBA'):5�_�                       "    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �               @def grading(score, break_points=[]60, 80, 90, ], grades='FCBA'):5�_�                       >    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �             5�_�                           ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �                      �                     5�_�                             ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �                  5�_�      !                      ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �                     index = bisect.bisect()5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �                      index = bisect.bisect_left()5�_�   !   #           "      %    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �                     return grades[]�                 %    index = bisect.bisect_left(score)5�_�   "   $           #           ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�    �                  #!/bin/usr/python       import bisect       ?def grading(score, break_points=[60, 80, 90, ], grades='FCBA'):   %    index = bisect.bisect_left(score)       return grades[index]5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�     �   	              print()�                  �               5�_�   $   &           %           ����                                                                                                                                                                                                                                                                                                                               
          
       V        _�    �               
   #!/bin/usr/python       import bisect           ?def grading(score, break_points=[60, 80, 90, ], grades='FCBA'):   %    index = bisect.bisect_left(score)       return grades[index]       print(grading(100))5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                               
          
       V        _     �      	             return grades[index]5�_�   &   (           '      $    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _
     �               %    index = bisect.bisect_left(score)5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                               
          
       V        _     �               %    index = bisect.bisect_left(score)5�_�   (   *           )          ����                                                                                                                                                                                                                                                                                                                               
          
       V        _#     �               %    index = bisect.bisect_left(score)5�_�   )   +           *          ����                                                                                                                                                                                                                                                                                                                               
          
       V        _&     �               &    index = bisect.bisect_left(,score)5�_�   *   ,           +      %    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _-     �               ,    index = bisect.bisect_left(grades,score)5�_�   +   -           ,           ����                                                                                                                                                                                                                                                                                                                               
          
       V        _4    �                  #!/bin/usr/python       import bisect           ?def grading(score, break_points=[60, 80, 90, ], grades='FCBA'):   2    index = bisect.bisect_left(break_points,score)       return grades[index]           print(grading(100))5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                               +                 V   +    _�     �   
              print(grading(100))5�_�   -   /           .          ����                                                                                                                                                                                                                                                                                                                               +                 V   +    _�    �   
              print(grading())5�_�   .               /          ����                                                                                                                                                                                                                                                                                                                               +                 V   +    _�    �               3    index = bisect.bisect_left(break_points, score)5�_�                       A    ����                                                                                                                                                                                                                                                                                                                               
          
       V        _V     �                Bdef grading(score, break_points=[0, 60, 80, 90, ], grades='FCBA'):       {}�                    {{}}5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       _     �                def ${1:function}(`!p   if snip.indent:   >    snip.rv = 'self' + (", " if len(t[2]) else "")`${2:arg1}):   E    `!p snip.rv = triple_quotes(snip)`${4:TODO: Docstring for $1.}`!p   #write_function_docstring(t, snip) `       ${5:${VISUAL:pass}}�         
      def function(`!p�         
      def function(${2:arg1}):�               def function(arg1):�                   TODO: Docstring for .`!p�                   TODO: Docstring for .�                    �               $    """TODO: Docstring for function.           :arg1: TODO       :returns: TODO           """�                    pass5��