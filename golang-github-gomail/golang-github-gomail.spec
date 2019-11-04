%global globalversion   2.0.0

%global goipath         github.com/go-gomail/gomail
%global tag             %{globalversion}
%global scm             git

%gometa

%global common_description %{expand:
Gomail is a simple and efficient package to send emails
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                %{globalversion}
Release:                1%{?dist}
Summary:                Gomail is a simple and efficient package to send emails

License:                MIT
URL:                    %{gourl}
Source0:                %{gosource}

Provides:               golang(gopkg.in/gomail.v2)


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
