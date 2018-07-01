if (self.CavalryLogger) { CavalryLogger.start_js(["mwPBS"]); }

__d("MessengerShareFilePreviewFunnelLoggerConstants",[],(function(a,b,c,d,e,f){"use strict";e.exports={CHAT_TAB:"chat_tab",MESSENGER_DOT_COM:"messenger_dot_com",PREPARE_FILES_FOR_SEND:"prepare_files_for_send",SHOW_FILE_PLACEHOLDER:"show_file_placeholder",UPLOAD_FILES_COMPLETE:"upload_files_complete",CANCEL_FILE_UPLOAD:"cancel_file_upload",UPLOAD_FILE_FAILED:"upload_file_failed"}}),null);
__d("MessengerShareFilePreviewFunnelLogger",["FunnelLogger","MessengerShareFilePreviewFunnelLoggerConstants"],(function(a,b,c,d,e,f){"use strict";__p&&__p();var g="WWW_MESSENGER_SHARE_FILE_PREVIEW_FUNNEL";function h(a){if(!a||typeof a!=="string"||!/^\w{3,12}:.+/.test(a))return 0;var b=a.indexOf(":");return parseInt(a.substr(b+1),10)}function a(a){if(!a)return;a=h(a);b("FunnelLogger").getFunnelInstance(g,a)||i(a)}function i(a){if(!a)return;b("FunnelLogger").startFunnel(g,a)}function c(a,c,d){if(!d)return;a=a?b("MessengerShareFilePreviewFunnelLoggerConstants").CHAT_TAB:b("MessengerShareFilePreviewFunnelLoggerConstants").MESSENGER_DOT_COM;b("FunnelLogger").appendActionWithPayload(g,h(d),c,{source:a})}function d(a){if(!a)return;b("FunnelLogger").endFunnel(g,h(a))}e.exports={appendAction:c,endFunnel:d,startFunnelIfNotStarted:a}}),null);