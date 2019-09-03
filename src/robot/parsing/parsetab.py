
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARGUMENT ARGUMENTS ASSIGN COMMENT_HEADER DATA DEFAULT_TAGS DOCUMENTATION END EOS ERROR FOR FORCE_TAGS FOR_SEPARATOR KEYWORD KEYWORD_HEADER LIBRARY METADATA NAME NON_DATA_TOKENS OLD_FOR_INDENT RESOURCE RETURN SETTING_HEADER SETUP SUITE_SETUP SUITE_TEARDOWN TAGS TEARDOWN TEMPLATE TESTCASE_HEADER TEST_SETUP TEST_TEARDOWN TEST_TEMPLATE TEST_TIMEOUT TIMEOUT VARIABLE VARIABLES VARIABLE_HEADERdatafile :\n                    | sectionssections : section\n                    | sections sectionsection : setting_section\n                   | variable_section\n                   | testcase_section\n                   | keyword_sectionsetting_section : setting_header EOS\n                           | setting_header EOS settingssetting_header : SETTING_HEADER\n                           | setting_header SETTING_HEADERsettings : setting\n                    | settings settingsetting : documentation_setting\n                   | suite_setup_setting EOS\n                   | suite_teardown_setting EOS\n                   | metadata_setting EOS\n                   | test_setup_setting EOS\n                   | test_teardown_setting EOS\n                   | test_template_setting EOS\n                   | test_timeout_setting EOS\n                   | force_tags_setting EOS\n                   | default_tags_setting EOS\n                   | library_setting EOS\n                   | resource_setting EOS\n                   | variables_setting EOS\n                   | setup_setting EOS\n                   | teardown_setting EOS\n                   | template_setting EOS\n                   | timeout_setting EOS\n                   | tags_setting EOS\n                   | arguments_setting EOS\n                   | return_setting EOSdocumentation_setting : DOCUMENTATION arguments EOSsuite_setup_setting : SUITE_SETUP argumentssuite_teardown_setting : SUITE_TEARDOWN argumentsmetadata_setting : METADATA argumentstest_setup_setting : TEST_SETUP argumentstest_teardown_setting : TEST_TEARDOWN argumentstest_template_setting : TEST_TEMPLATE argumentstest_timeout_setting : TEST_TIMEOUT argumentsforce_tags_setting : FORCE_TAGS argumentsdefault_tags_setting : DEFAULT_TAGS argumentslibrary_setting : LIBRARY argumentsresource_setting : RESOURCE argumentsvariables_setting : VARIABLES argumentssetup_setting : SETUP argumentsteardown_setting : TEARDOWN argumentstemplate_setting : TEMPLATE argumentstimeout_setting : TIMEOUT argumentstags_setting : TAGS argumentsarguments_setting : ARGUMENTS argumentsreturn_setting : RETURN argumentsvariable_section : variable_header EOS\n                            | variable_header EOS variablesvariable_header : VARIABLE_HEADER\n                           | variable_header VARIABLE_HEADERvariables : variable\n                     | variables variablevariable : VARIABLE arguments EOStestcase_section : testcase_header EOS\n                            | testcase_header EOS teststestcase_header : TESTCASE_HEADER\n                           | testcase_header TESTCASE_HEADERkeyword_section : keyword_header EOS\n                           | keyword_header EOS keywordskeyword_header : KEYWORD_HEADER\n                          | keyword_header KEYWORD_HEADERtests : test\n                 | tests testkeywords : keyword\n                    | keywords keywordtest : NAME EOS\n                | NAME EOS body_itemskeyword : NAME EOS\n                   | NAME EOS body_itemsbody_items : body_item\n                      | body_items body_itembody_item : forloop\n                     | setting\n                     | step\n                     | templatearguments\n                     | invalid_forloopstep : KEYWORD arguments EOSstep : assignments EOS\n                | assignments KEYWORD arguments EOSforloop : for_header for_body END EOS\n                   | for_header END EOS\n                   | END EOSfor_header : FOR arguments FOR_SEPARATOR arguments EOS\n                      | FOR arguments EOSfor_body : step\n                    | for_body step\n                    | templatearguments\n                    | for_body templateargumentstemplatearguments : arguments EOSinvalid_forloop : for_header for_bodyassignments : ASSIGN\n                       | assignments ASSIGNarguments : args\n                     | empty_argargs : ARGUMENT\n                | arguments ARGUMENTempty_arg : '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,16,17,19,21,23,25,26,27,67,68,70,71,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,119,121,122,123,124,125,127,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[-1,0,-2,-3,-5,-6,-7,-8,-4,-9,-55,-62,-66,-10,-13,-15,-56,-59,-63,-70,-67,-72,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-60,-71,-74,-73,-76,-35,-61,-75,-78,-80,-81,-82,-83,-84,-77,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'SETTING_HEADER':([0,2,3,4,5,6,7,8,12,16,17,18,19,21,23,25,26,27,67,68,70,71,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,119,121,122,123,124,125,127,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[12,12,-3,-5,-6,-7,-8,18,-11,-4,-9,-12,-55,-62,-66,-10,-13,-15,-56,-59,-63,-70,-67,-72,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-60,-71,-74,-73,-76,-35,-61,-75,-78,-80,-81,-82,-83,-84,-77,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'VARIABLE_HEADER':([0,2,3,4,5,6,7,9,13,16,17,19,20,21,23,25,26,27,67,68,70,71,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,119,121,122,123,124,125,127,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[13,13,-3,-5,-6,-7,-8,20,-57,-4,-9,-55,-58,-62,-66,-10,-13,-15,-56,-59,-63,-70,-67,-72,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-60,-71,-74,-73,-76,-35,-61,-75,-78,-80,-81,-82,-83,-84,-77,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'TESTCASE_HEADER':([0,2,3,4,5,6,7,10,14,16,17,19,21,22,23,25,26,27,67,68,70,71,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,119,121,122,123,124,125,127,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[14,14,-3,-5,-6,-7,-8,22,-64,-4,-9,-55,-62,-65,-66,-10,-13,-15,-56,-59,-63,-70,-67,-72,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-60,-71,-74,-73,-76,-35,-61,-75,-78,-80,-81,-82,-83,-84,-77,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'KEYWORD_HEADER':([0,2,3,4,5,6,7,11,15,16,17,19,21,23,24,25,26,27,67,68,70,71,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,119,121,122,123,124,125,127,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[15,15,-3,-5,-6,-7,-8,24,-68,-4,-9,-55,-62,-66,-69,-10,-13,-15,-56,-59,-63,-70,-67,-72,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-60,-71,-74,-73,-76,-35,-61,-75,-78,-80,-81,-82,-83,-84,-77,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'EOS':([8,9,10,11,12,13,14,15,18,20,22,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,72,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,122,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,],[17,19,21,23,-11,-57,-64,-68,-12,-58,-65,-69,-15,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,122,124,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,125,-101,-102,-103,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,127,-105,-105,-35,-104,-105,-78,-80,-81,-82,-83,-84,-105,148,-105,150,151,-105,-99,-105,-79,-98,158,-93,-95,-90,159,-97,-86,-105,-100,162,163,-94,-96,-89,-85,164,-105,-92,-88,-87,166,-91,]),'DOCUMENTATION':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[47,47,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,47,47,-35,47,-78,-80,-81,-82,-83,-84,47,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'SUITE_SETUP':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[48,48,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,48,48,-35,48,-78,-80,-81,-82,-83,-84,48,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'SUITE_TEARDOWN':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[49,49,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,49,49,-35,49,-78,-80,-81,-82,-83,-84,49,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'METADATA':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[50,50,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,50,50,-35,50,-78,-80,-81,-82,-83,-84,50,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'TEST_SETUP':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[51,51,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,51,51,-35,51,-78,-80,-81,-82,-83,-84,51,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'TEST_TEARDOWN':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[52,52,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,52,52,-35,52,-78,-80,-81,-82,-83,-84,52,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'TEST_TEMPLATE':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[53,53,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,53,53,-35,53,-78,-80,-81,-82,-83,-84,53,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'TEST_TIMEOUT':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[54,54,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,54,54,-35,54,-78,-80,-81,-82,-83,-84,54,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'FORCE_TAGS':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[55,55,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,55,55,-35,55,-78,-80,-81,-82,-83,-84,55,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'DEFAULT_TAGS':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[56,56,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,56,56,-35,56,-78,-80,-81,-82,-83,-84,56,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'LIBRARY':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[57,57,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,57,57,-35,57,-78,-80,-81,-82,-83,-84,57,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'RESOURCE':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[58,58,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,58,58,-35,58,-78,-80,-81,-82,-83,-84,58,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'VARIABLES':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[59,59,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,59,59,-35,59,-78,-80,-81,-82,-83,-84,59,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'SETUP':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[60,60,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,60,60,-35,60,-78,-80,-81,-82,-83,-84,60,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'TEARDOWN':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[61,61,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,61,61,-35,61,-78,-80,-81,-82,-83,-84,61,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'TEMPLATE':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[62,62,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,62,62,-35,62,-78,-80,-81,-82,-83,-84,62,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'TIMEOUT':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[63,63,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,63,63,-35,63,-78,-80,-81,-82,-83,-84,63,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'TAGS':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[64,64,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,64,64,-35,64,-78,-80,-81,-82,-83,-84,64,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'ARGUMENTS':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[65,65,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,65,65,-35,65,-78,-80,-81,-82,-83,-84,65,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'RETURN':([17,25,26,27,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[66,66,-13,-15,-14,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,66,66,-35,66,-78,-80,-81,-82,-83,-84,66,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'VARIABLE':([19,67,68,119,127,],[69,69,-59,-60,-61,]),'NAME':([21,23,27,70,71,73,74,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,121,122,123,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[72,75,-15,72,-70,75,-72,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-71,-74,-73,-76,-35,-75,-78,-80,-81,-82,-83,-84,-77,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'END':([27,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,135,142,143,144,146,147,148,150,151,156,157,158,159,162,163,164,166,],[-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,136,136,-35,136,-78,-80,-81,-82,-83,-84,145,136,-79,155,-93,-95,-90,-97,-86,-94,-96,-89,-85,-92,-88,-87,-91,]),'KEYWORD':([27,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,135,139,141,142,143,144,146,147,148,150,151,153,156,157,158,159,162,163,164,166,],[-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,137,137,-35,137,-78,-80,-81,-82,-83,-84,137,152,-99,137,-79,137,-93,-95,-90,-97,-86,-100,-94,-96,-89,-85,-92,-88,-87,-91,]),'FOR':([27,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,142,143,144,146,147,148,150,151,156,157,158,159,163,164,],[-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,140,140,-35,140,-78,-80,-81,-82,-83,-84,140,-79,-98,-93,-95,-90,-97,-86,-94,-96,-89,-85,-88,-87,]),'ASSIGN':([27,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,122,124,125,128,129,130,131,132,133,134,135,139,141,142,143,144,146,147,148,150,151,153,156,157,158,159,162,163,164,166,],[-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,141,141,-35,141,-78,-80,-81,-82,-83,-84,141,153,-99,141,-79,141,-93,-95,-90,-97,-86,-100,-94,-96,-89,-85,-92,-88,-87,-91,]),'ARGUMENT':([27,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,122,124,125,126,128,129,130,131,132,133,134,135,137,138,140,142,143,144,146,147,148,149,150,151,152,154,156,157,158,159,160,161,162,163,164,165,166,],[-15,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,126,-101,-102,-103,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,99,99,-35,-104,99,-78,-80,-81,-82,-83,-84,99,99,126,99,99,-79,99,-93,-95,-90,126,-97,-86,99,126,-94,-96,-89,-85,126,99,-92,-88,-87,126,-91,]),'FOR_SEPARATOR':([97,98,99,126,140,154,],[-101,-102,-103,-104,-105,161,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'datafile':([0,],[1,]),'sections':([0,],[2,]),'section':([0,2,],[3,16,]),'setting_section':([0,2,],[4,4,]),'variable_section':([0,2,],[5,5,]),'testcase_section':([0,2,],[6,6,]),'keyword_section':([0,2,],[7,7,]),'setting_header':([0,2,],[8,8,]),'variable_header':([0,2,],[9,9,]),'testcase_header':([0,2,],[10,10,]),'keyword_header':([0,2,],[11,11,]),'settings':([17,],[25,]),'setting':([17,25,122,124,128,142,],[26,76,131,131,131,131,]),'documentation_setting':([17,25,122,124,128,142,],[27,27,27,27,27,27,]),'suite_setup_setting':([17,25,122,124,128,142,],[28,28,28,28,28,28,]),'suite_teardown_setting':([17,25,122,124,128,142,],[29,29,29,29,29,29,]),'metadata_setting':([17,25,122,124,128,142,],[30,30,30,30,30,30,]),'test_setup_setting':([17,25,122,124,128,142,],[31,31,31,31,31,31,]),'test_teardown_setting':([17,25,122,124,128,142,],[32,32,32,32,32,32,]),'test_template_setting':([17,25,122,124,128,142,],[33,33,33,33,33,33,]),'test_timeout_setting':([17,25,122,124,128,142,],[34,34,34,34,34,34,]),'force_tags_setting':([17,25,122,124,128,142,],[35,35,35,35,35,35,]),'default_tags_setting':([17,25,122,124,128,142,],[36,36,36,36,36,36,]),'library_setting':([17,25,122,124,128,142,],[37,37,37,37,37,37,]),'resource_setting':([17,25,122,124,128,142,],[38,38,38,38,38,38,]),'variables_setting':([17,25,122,124,128,142,],[39,39,39,39,39,39,]),'setup_setting':([17,25,122,124,128,142,],[40,40,40,40,40,40,]),'teardown_setting':([17,25,122,124,128,142,],[41,41,41,41,41,41,]),'template_setting':([17,25,122,124,128,142,],[42,42,42,42,42,42,]),'timeout_setting':([17,25,122,124,128,142,],[43,43,43,43,43,43,]),'tags_setting':([17,25,122,124,128,142,],[44,44,44,44,44,44,]),'arguments_setting':([17,25,122,124,128,142,],[45,45,45,45,45,45,]),'return_setting':([17,25,122,124,128,142,],[46,46,46,46,46,46,]),'variables':([19,],[67,]),'variable':([19,67,],[68,119,]),'tests':([21,],[70,]),'test':([21,70,],[71,121,]),'keywords':([23,],[73,]),'keyword':([23,73,],[74,123,]),'arguments':([47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,122,124,128,135,137,140,142,144,152,161,],[96,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,138,138,138,138,149,154,138,138,160,165,]),'args':([47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,122,124,128,135,137,140,142,144,152,161,],[97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,97,]),'empty_arg':([47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,122,124,128,135,137,140,142,144,152,161,],[98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,]),'body_items':([122,124,],[128,142,]),'body_item':([122,124,128,142,],[129,129,143,143,]),'forloop':([122,124,128,142,],[130,130,130,130,]),'step':([122,124,128,135,142,144,],[132,132,132,146,132,156,]),'templatearguments':([122,124,128,135,142,144,],[133,133,133,147,133,157,]),'invalid_forloop':([122,124,128,142,],[134,134,134,134,]),'for_header':([122,124,128,142,],[135,135,135,135,]),'assignments':([122,124,128,135,142,144,],[139,139,139,139,139,139,]),'for_body':([135,],[144,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> datafile","S'",1,None,None,None),
  ('datafile -> <empty>','datafile',0,'p_datafile','parser.py',43),
  ('datafile -> sections','datafile',1,'p_datafile','parser.py',44),
  ('sections -> section','sections',1,'p_sections','parser.py',48),
  ('sections -> sections section','sections',2,'p_sections','parser.py',49),
  ('section -> setting_section','section',1,'p_section','parser.py',53),
  ('section -> variable_section','section',1,'p_section','parser.py',54),
  ('section -> testcase_section','section',1,'p_section','parser.py',55),
  ('section -> keyword_section','section',1,'p_section','parser.py',56),
  ('setting_section -> setting_header EOS','setting_section',2,'p_setting_section','parser.py',60),
  ('setting_section -> setting_header EOS settings','setting_section',3,'p_setting_section','parser.py',61),
  ('setting_header -> SETTING_HEADER','setting_header',1,'p_setting_header','parser.py',65),
  ('setting_header -> setting_header SETTING_HEADER','setting_header',2,'p_setting_header','parser.py',66),
  ('settings -> setting','settings',1,'p_settings','parser.py',69),
  ('settings -> settings setting','settings',2,'p_settings','parser.py',70),
  ('setting -> documentation_setting','setting',1,'p_setting','parser.py',74),
  ('setting -> suite_setup_setting EOS','setting',2,'p_setting','parser.py',75),
  ('setting -> suite_teardown_setting EOS','setting',2,'p_setting','parser.py',76),
  ('setting -> metadata_setting EOS','setting',2,'p_setting','parser.py',77),
  ('setting -> test_setup_setting EOS','setting',2,'p_setting','parser.py',78),
  ('setting -> test_teardown_setting EOS','setting',2,'p_setting','parser.py',79),
  ('setting -> test_template_setting EOS','setting',2,'p_setting','parser.py',80),
  ('setting -> test_timeout_setting EOS','setting',2,'p_setting','parser.py',81),
  ('setting -> force_tags_setting EOS','setting',2,'p_setting','parser.py',82),
  ('setting -> default_tags_setting EOS','setting',2,'p_setting','parser.py',83),
  ('setting -> library_setting EOS','setting',2,'p_setting','parser.py',84),
  ('setting -> resource_setting EOS','setting',2,'p_setting','parser.py',85),
  ('setting -> variables_setting EOS','setting',2,'p_setting','parser.py',86),
  ('setting -> setup_setting EOS','setting',2,'p_setting','parser.py',87),
  ('setting -> teardown_setting EOS','setting',2,'p_setting','parser.py',88),
  ('setting -> template_setting EOS','setting',2,'p_setting','parser.py',89),
  ('setting -> timeout_setting EOS','setting',2,'p_setting','parser.py',90),
  ('setting -> tags_setting EOS','setting',2,'p_setting','parser.py',91),
  ('setting -> arguments_setting EOS','setting',2,'p_setting','parser.py',92),
  ('setting -> return_setting EOS','setting',2,'p_setting','parser.py',93),
  ('documentation_setting -> DOCUMENTATION arguments EOS','documentation_setting',3,'p_documentation','parser.py',97),
  ('suite_setup_setting -> SUITE_SETUP arguments','suite_setup_setting',2,'p_suite_setup','parser.py',101),
  ('suite_teardown_setting -> SUITE_TEARDOWN arguments','suite_teardown_setting',2,'p_suite_teardown','parser.py',105),
  ('metadata_setting -> METADATA arguments','metadata_setting',2,'p_metadata','parser.py',109),
  ('test_setup_setting -> TEST_SETUP arguments','test_setup_setting',2,'p_test_setup','parser.py',113),
  ('test_teardown_setting -> TEST_TEARDOWN arguments','test_teardown_setting',2,'p_test_teardown','parser.py',117),
  ('test_template_setting -> TEST_TEMPLATE arguments','test_template_setting',2,'p_test_template','parser.py',121),
  ('test_timeout_setting -> TEST_TIMEOUT arguments','test_timeout_setting',2,'p_test_timeout','parser.py',125),
  ('force_tags_setting -> FORCE_TAGS arguments','force_tags_setting',2,'p_force_tags','parser.py',129),
  ('default_tags_setting -> DEFAULT_TAGS arguments','default_tags_setting',2,'p_default_tags','parser.py',133),
  ('library_setting -> LIBRARY arguments','library_setting',2,'p_library','parser.py',137),
  ('resource_setting -> RESOURCE arguments','resource_setting',2,'p_resource','parser.py',142),
  ('variables_setting -> VARIABLES arguments','variables_setting',2,'p_variables_import','parser.py',147),
  ('setup_setting -> SETUP arguments','setup_setting',2,'p_setup','parser.py',152),
  ('teardown_setting -> TEARDOWN arguments','teardown_setting',2,'p_teardown','parser.py',156),
  ('template_setting -> TEMPLATE arguments','template_setting',2,'p_template','parser.py',160),
  ('timeout_setting -> TIMEOUT arguments','timeout_setting',2,'p_timeout','parser.py',164),
  ('tags_setting -> TAGS arguments','tags_setting',2,'p_tags','parser.py',168),
  ('arguments_setting -> ARGUMENTS arguments','arguments_setting',2,'p_arguments_setting','parser.py',172),
  ('return_setting -> RETURN arguments','return_setting',2,'p_return','parser.py',176),
  ('variable_section -> variable_header EOS','variable_section',2,'p_variable_section','parser.py',180),
  ('variable_section -> variable_header EOS variables','variable_section',3,'p_variable_section','parser.py',181),
  ('variable_header -> VARIABLE_HEADER','variable_header',1,'p_variable_header','parser.py',185),
  ('variable_header -> variable_header VARIABLE_HEADER','variable_header',2,'p_variable_header','parser.py',186),
  ('variables -> variable','variables',1,'p_variables','parser.py',189),
  ('variables -> variables variable','variables',2,'p_variables','parser.py',190),
  ('variable -> VARIABLE arguments EOS','variable',3,'p_variable','parser.py',194),
  ('testcase_section -> testcase_header EOS','testcase_section',2,'p_testcase_section','parser.py',198),
  ('testcase_section -> testcase_header EOS tests','testcase_section',3,'p_testcase_section','parser.py',199),
  ('testcase_header -> TESTCASE_HEADER','testcase_header',1,'p_testcase_header','parser.py',203),
  ('testcase_header -> testcase_header TESTCASE_HEADER','testcase_header',2,'p_testcase_header','parser.py',204),
  ('keyword_section -> keyword_header EOS','keyword_section',2,'p_keyword_section','parser.py',208),
  ('keyword_section -> keyword_header EOS keywords','keyword_section',3,'p_keyword_section','parser.py',209),
  ('keyword_header -> KEYWORD_HEADER','keyword_header',1,'p_keyword_header','parser.py',213),
  ('keyword_header -> keyword_header KEYWORD_HEADER','keyword_header',2,'p_keyword_header','parser.py',214),
  ('tests -> test','tests',1,'p_tests','parser.py',217),
  ('tests -> tests test','tests',2,'p_tests','parser.py',218),
  ('keywords -> keyword','keywords',1,'p_keywords','parser.py',222),
  ('keywords -> keywords keyword','keywords',2,'p_keywords','parser.py',223),
  ('test -> NAME EOS','test',2,'p_test','parser.py',227),
  ('test -> NAME EOS body_items','test',3,'p_test','parser.py',228),
  ('keyword -> NAME EOS','keyword',2,'p_keyword','parser.py',235),
  ('keyword -> NAME EOS body_items','keyword',3,'p_keyword','parser.py',236),
  ('body_items -> body_item','body_items',1,'p_body_items','parser.py',243),
  ('body_items -> body_items body_item','body_items',2,'p_body_items','parser.py',244),
  ('body_item -> forloop','body_item',1,'p_body_item','parser.py',248),
  ('body_item -> setting','body_item',1,'p_body_item','parser.py',249),
  ('body_item -> step','body_item',1,'p_body_item','parser.py',250),
  ('body_item -> templatearguments','body_item',1,'p_body_item','parser.py',251),
  ('body_item -> invalid_forloop','body_item',1,'p_body_item','parser.py',252),
  ('step -> KEYWORD arguments EOS','step',3,'p_step','parser.py',256),
  ('step -> assignments EOS','step',2,'p_step_with_assignment','parser.py',260),
  ('step -> assignments KEYWORD arguments EOS','step',4,'p_step_with_assignment','parser.py',261),
  ('forloop -> for_header for_body END EOS','forloop',4,'p_forloop','parser.py',268),
  ('forloop -> for_header END EOS','forloop',3,'p_forloop','parser.py',269),
  ('forloop -> END EOS','forloop',2,'p_forloop','parser.py',270),
  ('for_header -> FOR arguments FOR_SEPARATOR arguments EOS','for_header',5,'p_for_header','parser.py',278),
  ('for_header -> FOR arguments EOS','for_header',3,'p_for_header','parser.py',279),
  ('for_body -> step','for_body',1,'p_for_body','parser.py',286),
  ('for_body -> for_body step','for_body',2,'p_for_body','parser.py',287),
  ('for_body -> templatearguments','for_body',1,'p_for_body','parser.py',288),
  ('for_body -> for_body templatearguments','for_body',2,'p_for_body','parser.py',289),
  ('templatearguments -> arguments EOS','templatearguments',2,'p_templatearguments','parser.py',293),
  ('invalid_forloop -> for_header for_body','invalid_forloop',2,'p_invalid_for_loop','parser.py',297),
  ('assignments -> ASSIGN','assignments',1,'p_assignments','parser.py',301),
  ('assignments -> assignments ASSIGN','assignments',2,'p_assignments','parser.py',302),
  ('arguments -> args','arguments',1,'p_arguments','parser.py',306),
  ('arguments -> empty_arg','arguments',1,'p_arguments','parser.py',307),
  ('args -> ARGUMENT','args',1,'p_args','parser.py',311),
  ('args -> arguments ARGUMENT','args',2,'p_args','parser.py',312),
  ('empty_arg -> <empty>','empty_arg',0,'p_empty_arg','parser.py',316),
]