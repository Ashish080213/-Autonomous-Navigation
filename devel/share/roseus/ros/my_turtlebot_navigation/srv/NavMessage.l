;; Auto-generated. Do not edit!


(when (boundp 'my_turtlebot_navigation::NavMessage)
  (if (not (find-package "MY_TURTLEBOT_NAVIGATION"))
    (make-package "MY_TURTLEBOT_NAVIGATION"))
  (shadow 'NavMessage (find-package "MY_TURTLEBOT_NAVIGATION")))
(unless (find-package "MY_TURTLEBOT_NAVIGATION::NAVMESSAGE")
  (make-package "MY_TURTLEBOT_NAVIGATION::NAVMESSAGE"))
(unless (find-package "MY_TURTLEBOT_NAVIGATION::NAVMESSAGEREQUEST")
  (make-package "MY_TURTLEBOT_NAVIGATION::NAVMESSAGEREQUEST"))
(unless (find-package "MY_TURTLEBOT_NAVIGATION::NAVMESSAGERESPONSE")
  (make-package "MY_TURTLEBOT_NAVIGATION::NAVMESSAGERESPONSE"))

(in-package "ROS")





(defclass my_turtlebot_navigation::NavMessageRequest
  :super ros::object
  :slots (_label ))

(defmethod my_turtlebot_navigation::NavMessageRequest
  (:init
   (&key
    ((:label __label) "")
    )
   (send-super :init)
   (setq _label (string __label))
   self)
  (:label
   (&optional __label)
   (if __label (setq _label __label)) _label)
  (:serialization-length
   ()
   (+
    ;; string _label
    4 (length _label)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _label
       (write-long (length _label) s) (princ _label s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _label
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _label (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass my_turtlebot_navigation::NavMessageResponse
  :super ros::object
  :slots (_navigation_successfull _message ))

(defmethod my_turtlebot_navigation::NavMessageResponse
  (:init
   (&key
    ((:navigation_successfull __navigation_successfull) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _navigation_successfull __navigation_successfull)
   (setq _message (string __message))
   self)
  (:navigation_successfull
   (&optional (__navigation_successfull :null))
   (if (not (eq __navigation_successfull :null)) (setq _navigation_successfull __navigation_successfull)) _navigation_successfull)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _navigation_successfull
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _navigation_successfull
       (if _navigation_successfull (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _navigation_successfull
     (setq _navigation_successfull (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass my_turtlebot_navigation::NavMessage
  :super ros::object
  :slots ())

(setf (get my_turtlebot_navigation::NavMessage :md5sum-) "920ca5ca095e1b5230fc32da338a974c")
(setf (get my_turtlebot_navigation::NavMessage :datatype-) "my_turtlebot_navigation/NavMessage")
(setf (get my_turtlebot_navigation::NavMessage :request) my_turtlebot_navigation::NavMessageRequest)
(setf (get my_turtlebot_navigation::NavMessage :response) my_turtlebot_navigation::NavMessageResponse)

(defmethod my_turtlebot_navigation::NavMessageRequest
  (:response () (instance my_turtlebot_navigation::NavMessageResponse :init)))

(setf (get my_turtlebot_navigation::NavMessageRequest :md5sum-) "920ca5ca095e1b5230fc32da338a974c")
(setf (get my_turtlebot_navigation::NavMessageRequest :datatype-) "my_turtlebot_navigation/NavMessageRequest")
(setf (get my_turtlebot_navigation::NavMessageRequest :definition-)
      "# request
string label
---
#response
bool navigation_successfull
string message
")

(setf (get my_turtlebot_navigation::NavMessageResponse :md5sum-) "920ca5ca095e1b5230fc32da338a974c")
(setf (get my_turtlebot_navigation::NavMessageResponse :datatype-) "my_turtlebot_navigation/NavMessageResponse")
(setf (get my_turtlebot_navigation::NavMessageResponse :definition-)
      "# request
string label
---
#response
bool navigation_successfull
string message
")



(provide :my_turtlebot_navigation/NavMessage "920ca5ca095e1b5230fc32da338a974c")


