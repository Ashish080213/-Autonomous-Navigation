
(cl:in-package :asdf)

(defsystem "my_turtlebot_navigation-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "NavMessage" :depends-on ("_package_NavMessage"))
    (:file "_package_NavMessage" :depends-on ("_package"))
  ))