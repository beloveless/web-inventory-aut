    FROM ubuntu:18.04

    ENV DEBIAN_FRONTEND=noninteractive

    # Install dependencies
    RUN apt-get update  > /dev/null && \
    apt-get install -y \
            software-properties-common \
            apt-transport-https \
            git \
            gcc \
            make \
            re2c \
            apache2 \
            apache2-utils > /dev/null

    # Add PHP PPA for additional PHP versions
    RUN add-apt-repository -y ppa:ondrej/php

    # Update dependencies
    RUN apt-get update > /dev/null

    # Install specific PHP version and other packages
    RUN apt-get install -y php7.2 \
            php7.2-json \
            php7.2-dev \
            libpcre3-dev \
            php7.2-mysql \
            curl \
            libboost-all-dev > /dev/null && \
            a2enmod rewrite > /dev/null
    
    # Clone PHP-CPP repository
    RUN git clone https://github.com/CopernicaMarketingSoftware/PHP-CPP.git ./PHP-CPP \
            && cd ./PHP-CPP \
            && make -s \
            && make install -s

    # Install PHPCrypfish
    RUN git clone https://github.com/beloveless/NGPHPCrypfish-code.git \
            && cd ./NGPHPCrypfish-code \
            && make clean -s \
            && make -s \
            && make install -s \
            && phpenmod -v 7.2 phpcrypfish 

    # Set working directory
    WORKDIR /var/www/html
    RUN rm -rf *

    EXPOSE 80

    CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]